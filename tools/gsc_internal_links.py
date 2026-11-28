#!/usr/bin/env python3
"""Page-2 keyword internal-link boost (BLUEPRINT §12.4). Anwar, Nov 2 2026.

Search Console, Oct 3-31 2026: queries at position 11-20 with the most impressions.
For each target page, 3 relevant pages get a contextual sentence with a keyword-rich
anchor, placed in their intro section (not the footer). Idempotent: each link sits
between <!-- gsc-link:<target> --> markers and is replaced on re-run.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# target: (keyword, avg position, impressions) -> [(source page, sentence with {a}…{/a})]
LINKS = {
    "intercom-installation-nyc": [  # building intercom nyc 20 / intercom installation nyc 17.1 / commercial intercoms nyc 16.7
        ("intercom-installation-brooklyn-new-york",
         "Managing more than one property? We handle {a}building intercom installation across NYC{/a}, so every building in your portfolio runs on the same system and the same service team."),
        ("intercom-installation-manhattan-ny",
         "Outside Manhattan too, our {a}intercom installation in NYC{/a} covers co-ops, condos, rentals and offices in all five boroughs."),
        ("intercom-installation-queens-ny",
         "For offices, retail and mixed-use buildings, see our {a}commercial intercoms in NYC{/a}: video entry, phone-app answering and door release tied into access control."),
    ],
    "intercom-repair-nyc": [  # intercom replacement nyc 11.7
        ("intercom-repair-manhattan",
         "When the old panel isn't worth fixing anymore, we handle {a}intercom replacement in NYC{/a} and reuse the building's existing wiring wherever it tests good."),
        ("intercom-repair-brooklyn",
         "If your system keeps breaking down, compare repair against a full {a}intercom repair or replacement anywhere in NYC{/a} before you pay for another patch."),
        ("door-buzzer-repair-nyc",
         "Buzzer dead and the whole intercom aging out? Our {a}NYC intercom repair and replacement{/a} team swaps tired systems for modern video entry."),
    ],
    "alarm-installation-nyc": [  # alarm systems nyc 13.3 / alarm monitoring nyc 17.3
        ("alarm-installation-brooklyn",
         "We install and monitor {a}alarm systems across NYC{/a}, with 24/7 central-station alarm monitoring and phone-app control."),
        ("alarm-installation-manhattan",
         "Need coverage beyond Manhattan? Our {a}NYC alarm installation and alarm monitoring{/a} service covers homes and businesses in every borough."),
        ("home-automation-installation-nyc",
         "Automation works best with a monitored alarm behind it. See our {a}alarm systems in NYC{/a}, which link to the same app that controls your lights and locks."),
    ],
    "alarm-installation-queens": [  # home security systems in queens, ny 15.1
        ("security-camera-installation-queens",
         "Pair your cameras with {a}home security systems in Queens, NY{/a}: door and window sensors, motion detectors and 24/7 monitoring on one app."),
        ("access-control-installation-queens",
         "For full coverage, add one of our {a}home and business security systems in Queens{/a} to your access control: alarms, sensors and central-station monitoring."),
        ("intercom-installation-queens-ny",
         "Completing your building's protection? We also install {a}security alarm systems in Queens, NY{/a} for homes, stores and multi-family buildings."),
    ],
    "home-automation-installation-long-island": [  # home automation long island 18.8 / control4 smart home long island 10.7
        ("av-sound-installation-long-island",
         "Want one app for your audio, lights, shades and locks? See our {a}home automation on Long Island{/a}, including Control4 smart-home systems."),
        ("alarm-installation-long-island",
         "Your alarm can control more than sensors. Our {a}Long Island home automation{/a} links lights, locks, thermostats and cameras to the same system."),
        ("home-automation-installation-nassau-county",
         "Serving Suffolk too, our {a}home automation installation across Long Island{/a} covers Control4 and smart-home packages from Great Neck to Montauk."),
    ],
    "av-sound-installation-long-island": [  # home theater installation long island ny 18.7 / av installation in long island 11.9
        ("tv-installation-long-island",
         "Going beyond a mounted TV? Our {a}home theater and AV installation on Long Island{/a} adds surround sound, multi-room audio and hidden wiring."),
        ("home-automation-installation-long-island",
         "Automation pairs naturally with our {a}AV installation in Long Island, NY{/a}: home theaters, whole-house audio and media rooms on one remote."),
        ("av-sound-installation-nassau-county",
         "Live in Suffolk? Our {a}Long Island home theater installation{/a} team designs and installs AV systems across both counties."),
    ],
}

A0 = "<!-- gsc-link:{t} -->"
A1 = "<!-- /gsc-link:{t} -->"


def apply(src, links):
    """Strip every gsc-link block from the page, then re-insert this run's blocks in order."""
    path = os.path.join(ROOT, src + ".html")
    if not os.path.isfile(path):
        return False
    html = open(path, encoding="utf-8").read()
    html2 = re.sub(r"\n?<!-- gsc-link:([\w-]+) -->.*?<!-- /gsc-link:\1 -->\n?", "", html, flags=re.S)
    # first real body paragraph: plain <p>, <p class="bt"> or a styled prose <p>, 200+ chars of text
    start = html2.find("<body")
    m = None
    for c in re.finditer(r'<p( class="bt")?( style="[^"]*line-height[^"]*")?>(.*?)</p>', html2[start:], re.S):
        if len(re.sub(r"<[^>]+>", "", c.group(3))) >= 200:
            m = c
            break
    if not m:
        return False
    opener = m.group(0)[:m.group(0).find(">") + 1]
    end = start + m.end()
    wrapped = html2[end:end + 6] == "</div>"
    if wrapped:
        end += 6
    blocks = ""
    for target, sentence in links:
        body = sentence.replace("{a}", f'<a href="/{target}">').replace("{/a}", "</a>")
        para = f"{opener}{body}</p>"
        if wrapped:
            para = '<div class="rv">' + para + "</div>"
        blocks += "\n" + A0.format(t=target) + para + A1.format(t=target)
    new = html2[:end] + blocks + "\n" + html2[end:]
    if new != html:
        open(path, "w", encoding="utf-8").write(new)
        return True
    return False


def main():
    by_src = {}
    for target, rows in LINKS.items():
        for src, sentence in rows:
            if src != target:
                by_src.setdefault(src, []).append((target, sentence))
    n = sum(apply(src, links) for src, links in by_src.items())
    print(f"gsc_internal_links: {n} files updated")


if __name__ == "__main__":
    main()
