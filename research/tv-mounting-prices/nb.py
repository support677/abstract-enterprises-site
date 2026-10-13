# neighborhood cost-driver tables for spoke pages (65-inch flat/tilt job, labor; Manhattan includes $150 parking)
def r(base, pk, *walls):
    W={'dry':0,'metal':30,'plaster':45,'brick':65,'concrete':75}
    v=sorted(base+30+W[w]+pk for w in walls)
    return '$%.2f' % v[0] if v[0]==v[-1] else '$%.2f&ndash;$%.2f' % (v[0], v[-1])
def NB(k, base, pk):
    D={
 'brooklyn':[
  ('Park Slope','Brownstones and row houses','Plaster over brick',('plaster',)),
  ('Brooklyn Heights','19th-century brownstones, prewar co-ops','Plaster over brick',('plaster',)),
  ('Bed-Stuy','Brownstones and row houses','Plaster; brick on party walls',('plaster','brick')),
  ('Crown Heights','Prewar elevator buildings, row houses','Plaster',('plaster',)),
  ('East Flatbush &amp; Canarsie (closest to our Troy Ave shop)','Brick row houses and two-families','Drywall over wood studs, some plaster',('dry','plaster')),
  ('Flatbush &amp; Ditmas Park','Prewar elevator buildings, detached Victorian houses','Plaster or drywall',('dry','plaster')),
  ('Williamsburg','Converted lofts and newer glass towers','Exposed brick or metal studs',('metal','brick')),
  ('Greenpoint','Wood-frame row houses, waterfront towers','Drywall over wood or metal studs',('dry','metal')),
  ('Bushwick','Row houses and loft conversions','Drywall or exposed brick',('dry','brick')),
  ('DUMBO','Warehouse lofts','Brick and concrete',('brick','concrete')),
  ('Downtown Brooklyn','Newer high-rises','Metal studs; concrete columns',('metal','concrete')),
  ('Sunset Park','Row houses and industrial lofts','Plaster or brick',('plaster','brick')),
  ('Bay Ridge','Prewar co-ops, row houses, detached homes','Plaster; brick fireplaces',('plaster',)),
  ('Bensonhurst &amp; Dyker Heights','Two-families and detached houses','Drywall over wood studs',('dry',)),
  ('Sheepshead Bay &amp; Marine Park','Detached houses, finished basements','Drywall over wood studs',('dry',)),
  ('Coney Island &amp; Brighton Beach','High-rise co-ops and rentals','Concrete or metal studs',('metal','concrete'))],
 'queens':[
  ('Astoria','Brick two-families, prewar apartment buildings','Drywall or plaster',('dry','plaster')),
  ('Long Island City','Glass residential towers','Metal studs; concrete columns',('metal','concrete')),
  ('Sunnyside &amp; Woodside','Prewar buildings, garden co-ops','Plaster',('plaster',)),
  ('Jackson Heights','Prewar garden co-ops','Plaster',('plaster',)),
  ('Elmhurst &amp; Corona','Two-families and apartment buildings','Drywall or plaster',('dry','plaster')),
  ('Ridgewood','Brick row flats','Plaster over brick',('plaster',)),
  ('Rego Park','Postwar elevator co-ops','Plaster or concrete',('plaster','concrete')),
  ('Forest Hills','Prewar co-ops, Tudor-style houses','Plaster; stone fireplaces',('plaster',)),
  ('Flushing','High-rise condos and older houses','Metal studs or drywall',('dry','metal')),
  ('Bayside','Detached houses','Drywall over wood studs; brick fireplaces',('dry',)),
  ('Whitestone &amp; College Point','Detached and semi-detached houses','Drywall over wood studs',('dry',)),
  ('Fresh Meadows','Garden apartments and houses','Drywall',('dry',)),
  ('Jamaica &amp; Jamaica Estates','Detached houses, newer rentals','Drywall or metal studs',('dry','metal')),
  ('Howard Beach &amp; the Rockaways','Houses and beach-block co-ops','Drywall or concrete',('dry','concrete'))],
 'manhattan':[
  ('Upper East Side','Prewar co-ops, postwar white-brick towers','Plaster or concrete',('plaster','concrete')),
  ('Upper West Side','Prewar co-ops and brownstones','Plaster',('plaster',)),
  ('Harlem','Brownstones and newer rentals','Plaster over brick or metal studs',('metal','plaster')),
  ('Washington Heights &amp; Inwood','Prewar walk-ups and elevator buildings','Plaster (add $40 for a walk-up above the 2nd floor)',('plaster',)),
  ('Midtown','Offices, hotels, glass condos','Metal studs or concrete',('metal','concrete')),
  ('Hell&#x2019;s Kitchen','Tenement walk-ups and new towers','Plaster over brick or metal studs',('metal','plaster')),
  ('Chelsea','Lofts and new condos','Brick or metal studs',('metal','brick')),
  ('Murray Hill &amp; Gramercy','Postwar doorman buildings','Concrete or plaster',('plaster','concrete')),
  ('Greenwich Village &amp; West Village','Townhouses and prewar co-ops','Plaster or brick',('plaster','brick')),
  ('East Village &amp; Lower East Side','Tenement walk-ups','Plaster over brick (add $40 for a walk-up above the 2nd floor)',('plaster','brick')),
  ('SoHo &amp; Tribeca','Cast-iron and loft buildings','Brick or concrete',('brick','concrete')),
  ('Financial District','Office-to-residential conversions','Concrete or metal studs',('metal','concrete')),
  ('Battery Park City','Newer high-rises','Concrete or metal studs',('metal','concrete')),
  ('Morningside Heights','Prewar co-ops and university housing','Plaster',('plaster',)),
  ('East Harlem','Walk-ups and newer rentals','Plaster or drywall over metal studs',('metal','plaster')),
  ('Turtle Bay &amp; Tudor City','Prewar co-ops','Plaster',('plaster',)),
  ('Flatiron &amp; NoMad','Loft and office buildings','Brick or concrete',('brick','concrete')),
  ('Hudson Yards','Newer glass towers','Metal studs or concrete',('metal','concrete')),
  ('Roosevelt Island','High-rise rentals and condos','Concrete or metal studs',('metal','concrete'))]}[k]
    return [(n,h,w,r(base,pk,*ws)) for n,h,w,ws in D]
