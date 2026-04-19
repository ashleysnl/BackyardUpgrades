from pathlib import Path
import csv, json, textwrap, zipfile

root = Path('/mnt/data/backyard_publish_handoff')
articles_dir = root / 'content' / 'articles'
legal_dir = root / 'content' / 'legal'
data_dir = root / 'data'
docs_dir = root / 'docs'

TAG = 'simplekit-20'

def search_link(query):
    from urllib.parse import quote_plus
    return f'https://www.amazon.ca/s?k={quote_plus(query)}&tag={TAG}'

def dp_link(asin):
    return f'https://www.amazon.ca/dp/{asin}?tag={TAG}'

products = [
    # Lighting
    ['best-solar-lights-canada','Nymphy Solar Spot Lights 4-Pack','solar spotlight','Recent Amazon bestseller coverage for bright, adjustable landscape lighting.',search_link('Nymphy solar spot lights 4 pack outdoor')],
    ['best-solar-lights-canada','Gigalumi Solar Pathway Lights 12-Pack','solar pathway light','Recent coverage highlighted these as an affordable path-light option.',search_link('Gigalumi solar pathway lights 12 pack')],
    ['best-solar-lights-canada','Addlon Solar String Lights','solar string light','Useful for patios where ambiance matters more than wayfinding.',search_link('Addlon solar string lights outdoor')],

    ['backyard-lighting-under-100','Addlon 48FT Outdoor String Lights','plug-in string light','Frequently cited as a strong value pick for patios and pergolas.',search_link('Addlon 48FT outdoor string lights')],
    ['backyard-lighting-under-100','Brightech Ambience Pro Solar String Lights','solar string light','Widely recommended when you want no extension cord.',search_link('Brightech Ambience Pro solar string lights')],
    ['backyard-lighting-under-100','Brightown Globe String Lights','globe patio light','Budget-friendly decorative patio lighting option.',search_link('Brightown globe string lights outdoor')],

    # Fire pits
    ['best-fire-pits-canada','Solo Stove Bonfire 2.0','smokeless fire pit','Consistently recommended for cleaner burns and easier cleanup.',search_link('Solo Stove Bonfire 2.0 smokeless fire pit')],
    ['best-fire-pits-canada','Outland Living Mega Fire Pit','propane fire pit','Frequently recommended gas option for simple, smoke-free use.',search_link('Outland Living Mega propane fire pit')],
    ['best-fire-pits-canada','Amazon Basics Steel Lattice Fire Pit','budget wood fire pit','Budget pick mentioned in current fire-pit testing coverage.',search_link('Amazon Basics steel lattice fire pit')],

    ['propane-vs-wood-fire-pit','Outland Living Mega Fire Pit','propane fire pit','Easy-start propane option for lower-maintenance buyers.',search_link('Outland Living Mega propane fire pit')],
    ['propane-vs-wood-fire-pit','Solo Stove Bonfire 2.0','wood smokeless fire pit','Strong wood-burning option with reduced smoke.',search_link('Solo Stove Bonfire 2.0 smokeless fire pit')],
    ['propane-vs-wood-fire-pit','Fire pit cover 30 inch round','accessory','Weather protection accessory for longer service life.',search_link('30 inch round fire pit cover outdoor')],

    # Gardening
    ['raised-garden-beds-canada','Keter Maple Raised Garden Bed','raised garden bed','Weather-resistant resin raised bed sold in Canada.',search_link('Keter Maple Raised Garden Bed')],
    ['raised-garden-beds-canada','Galvanized Steel Raised Garden Bed','raised garden bed','Standard budget-friendly cold-climate bed style.',search_link('galvanized steel raised garden bed outdoor')],
    ['raised-garden-beds-canada','Garden bed cover hoops and mesh','accessory','Useful for frost, pests, and seedling protection.',search_link('raised garden bed hoops cover mesh')],

    ['beginner-garden-setup','Keter Maple Raised Garden Bed','raised garden bed','Simple starter bed for beginners.',search_link('Keter Maple Raised Garden Bed')],
    ['beginner-garden-setup','Seed starter trays with humidity dome','starter kit','Helps extend the short season indoors.',search_link('seed starter trays with humidity dome')],
    ['beginner-garden-setup','Garden hose timer','watering','Helps beginners stay consistent with watering.',search_link('garden hose timer outdoor')],

    # Smart backyard
    ['smart-backyard-setup','Amazon Smart Plug','smart plug','Exact Amazon Canada product page found; indoor only.',dp_link('B089DTMHW4')],
    ['smart-backyard-setup','Amazon Basics Outdoor Smart Plug','outdoor smart plug','Good fit for Alexa-based outdoor automation.',search_link('Amazon Basics Outdoor Smart Plug Alexa')],
    ['smart-backyard-setup','TP-Link Tapo C500 Outdoor Camera','outdoor camera','Outdoor camera option with pan/tilt coverage.',search_link('TP-Link Tapo C500 outdoor camera')],

    ['automate-backyard-lighting','Amazon Basics Outdoor Smart Plug','outdoor smart plug','Simple way to automate exterior lighting circuits.',search_link('Amazon Basics Outdoor Smart Plug Alexa')],
    ['automate-backyard-lighting','Amazon Smart Plug','indoor smart plug','Best for sheltered indoor-controlled plug points.',dp_link('B089DTMHW4')],
    ['automate-backyard-lighting','Smart LED outdoor string lights','smart string light','Good for app-based scenes and timers.',search_link('smart LED outdoor string lights Alexa')],

    # Comfort
    ['cozy-backyard-setup','Addlon 48FT Outdoor String Lights','string lights','Ambient lighting anchor for a cozy setup.',search_link('Addlon 48FT outdoor string lights')],
    ['cozy-backyard-setup','Outdoor throw blanket waterproof backed','textile','Useful shoulder-season comfort add-on.',search_link('outdoor throw blanket waterproof backed')],
    ['cozy-backyard-setup','Portable propane patio heater','heater','Adds shoulder-season warmth where a fire pit is not practical.',search_link('portable propane patio heater outdoor')],

    ['small-backyard-transformation','Keter raised planter box','planter','Vertical or compact planting helps small spaces work harder.',search_link('Keter raised planter box')],
    ['small-backyard-transformation','Outdoor storage bench deck box','storage','Adds hidden storage while doubling as seating.',search_link('outdoor storage bench deck box')],
    ['small-backyard-transformation','Addlon 48FT Outdoor String Lights','lighting','Creates height and ambiance without eating floor area.',search_link('Addlon 48FT outdoor string lights')],
]

articles = [
    {
        'slug':'best-solar-lights-canada','title':'Best Solar Lights for Canadian Backyards','category':'Lighting','deck':'A practical guide to choosing solar lights that survive real backyard use and make paths, patios, and garden beds more usable after dark.','readTime':'8 min read','featured':True,
        'body': '''
# Best Solar Lights for Canadian Backyards

Solar lighting works well in Canada when you match the product to the job. The mistake most people make is buying one style of light and trying to use it everywhere. Path lights, spot lights, deck lights, and patio string lights all solve different problems.

## What matters most in Canada

Canadian backyards put lighting through a harder test than a sheltered patio in a warm climate. You are dealing with freeze-thaw cycles, wind, snow load, spring rain, and long periods of lower winter daylight. That means the best pick is not always the fanciest-looking light. It is the one you can install quickly, leave outside, and trust to keep working.

Look for four basics first:

- A housing that feels solid rather than brittle.
- A clear use case such as path lighting, accent lighting, or ambiance.
- Easy replacement or repositioning if one spot gets poor charging.
- Reviews or product notes that speak to outdoor durability.

## Best overall for landscape highlighting

**Nymphy Solar Spot Lights** are a strong fit when you want brighter light on shrubs, flagpoles, garden beds, or the side of the house. Spot lights are better than path lights when you want to create depth and highlight landscaping instead of just marking a walkway.

**Best for:** feature lighting, garden beds, foundation planting, and darker corners of the yard.

## Best for walkways and front-to-backyard traffic

**Gigalumi Solar Pathway Lights** make the most sense when the goal is simple: make paths easier to follow and keep the yard feeling finished after sunset. These are the lights that work well along stepping stones, driveway edges, or a straight line from deck to shed.

**Best for:** pathways, edging, and low-glare decorative lighting.

## Best for patio mood lighting

**Addlon Solar String Lights** are the style to use when you care more about atmosphere than ground visibility. They are ideal for pergolas, fences, privacy screens, and covered sitting areas. A backyard with a seating zone almost always benefits from one layer of overhead or perimeter light.

**Best for:** patios, pergolas, dining areas, and evening entertaining.

## How to choose the right light type

### Choose path lights if:
- You want safe, low-level guidance along a route.
- You want fast installation with almost no planning.
- You want the yard to look tidy and finished.

### Choose spot lights if:
- You want more visible output.
- You want to show off landscaping or architectural details.
- You want one fixture to do more work.

### Choose string lights if:
- You spend time sitting, eating, or hosting outdoors.
- You want the yard to feel warmer and more premium.
- You already have enough functional lighting elsewhere.

## Placement tips that matter more than the product

A decent solar light in a good location will usually outperform a premium light in a bad one. Avoid placing stakes where they spend half the day behind fences, sheds, or dense shrubs. If your best-looking spot gets poor sun, move the light and light the area indirectly instead of forcing a bad placement.

For pathways, keep spacing consistent. For accent lights, aim them across a feature instead of directly up the middle of it. For patios, hang string lights lower than you think if the goal is warmth and intimacy, but high enough that you do not create a glare line.

## The smart way to buy

For most homeowners, the best backyard mix is not one product. It is:

1. Path lights for circulation.
2. One or two spot lights for landscaping.
3. One string-light run over the sitting area.

That combination gives you function and atmosphere without overspending.

## Final recommendation

If you are starting from zero, buy path lights first if your yard lacks visibility, or string lights first if your yard already works but feels flat at night. Then add spot lights where you want more drama. That staged approach is cheaper, simpler, and usually better looking than buying one large matching bundle.

## Recommended products

- **Nymphy Solar Spot Lights 4-Pack** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_1)
- **Gigalumi Solar Pathway Lights 12-Pack** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_2)
- **Addlon Solar String Lights** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_3)
'''
    },
    {
        'slug':'backyard-lighting-under-100','title':'Backyard Lighting Under $100','category':'Lighting','deck':'Affordable lighting combinations that make a backyard feel more finished without forcing a full renovation budget.','readTime':'7 min read','featured':False,
        'body': '''
# Backyard Lighting Under $100

You do not need a full landscape lighting plan to make a backyard look dramatically better at night. Most small and mid-size yards improve fast with one of three moves: add overhead glow, improve path visibility, or layer a few low-cost accents where the eye naturally lands.

## The under-$100 rule

When the budget is tight, the goal is not to light everything. The goal is to make the yard feel intentional. That usually means picking one primary zone:

- the patio or deck
- the path to the yard
- a small garden or feature wall

Trying to stretch a small budget across the whole property usually creates a weak result.

## Best value for patio atmosphere

**Addlon 48FT Outdoor String Lights** are a good anchor buy because they change the mood of a space immediately. If you have a pergola, fence corner, deck railing, or shepherd hooks, string lights do more visual work per dollar than almost anything else.

## Best off-grid option

**Brightech Ambience Pro Solar String Lights** make sense when you do not want to run extension cords or outdoor power. They are especially useful for small patios, rental properties, and areas where a clean install matters more than maximum brightness.

## Best decorative filler under budget

**Brightown Globe String Lights** are a good choice for smaller spaces where you want a softer, decorative look. They also work as a second layer when your main yard lighting already exists.

## Three budget-friendly lighting plans

### Plan 1: Patio-first
Buy one main string-light set and spend the rest on mounting hardware or hooks. This works best when your backyard activity is mostly sitting, eating, or entertaining.

### Plan 2: Path-first
Use most of the budget on path lights, then add one cheap decorative strand on a fence or railing. This works best when the yard feels dark and inconvenient to walk through.

### Plan 3: One focal point
Light one tree, planter wall, privacy screen, or pergola corner. A well-lit focal point can make the entire yard feel upgraded.

## Where budget lighting usually goes wrong

- Buying lights that are too blue or harsh.
- Mixing too many styles in one small space.
- Ignoring mounting and spacing.
- Choosing brightness over comfort in seating areas.

A cheaper warm light in the right position usually looks better than a brighter, harsher fixture placed badly.

## Best shopping strategy

Start with your highest-use zone. If you are outside on the patio every evening, that is the first money to spend. If you are constantly walking from the house to the shed, gate, or hot tub, improve that route first.

Under $100, the winning move is almost always one strong change rather than four weak ones.

## Final recommendation

If your yard is mostly for relaxing, buy string lights. If it is mostly about function, buy path lighting. If it already works and just feels bland, add one decorative layer where people gather and stop there.

## Recommended products

- **Addlon 48FT Outdoor String Lights** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_1)
- **Brightech Ambience Pro Solar String Lights** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_2)
- **Brightown Globe String Lights** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_3)
'''
    },
    {
        'slug':'best-fire-pits-canada','title':'Best Fire Pits for Windy Backyards','category':'Fire Pits','deck':'Which fire pit styles hold up better when your backyard gets real wind, and which tradeoffs actually matter before you buy.','readTime':'8 min read','featured':True,
        'body': '''
# Best Fire Pits for Windy Backyards

Wind changes everything. A fire pit that looks great in a showroom or on a calm summer deck can become annoying fast in an exposed yard. Smoke direction matters more. Ignition matters more. Flame control matters more. And cleanup matters a lot more when ash ends up everywhere.

## First decision: wood or propane

In a windy backyard, propane is usually easier to live with. It starts quickly, avoids ash blow-around, and lets you shut things down cleanly. Wood still wins on smell, sound, and traditional campfire feel, but it demands better placement and more tolerance for mess.

## Best wood option for cleaner burns

**Solo Stove Bonfire 2.0** is the wood fire pit I would put first on the shortlist if you want a better chance of staying comfortable in breezy conditions. The smokeless design does not make wind irrelevant, but it reduces one of the biggest frustrations of backyard fires: constant smoke chasing.

## Best propane option for easy use

**Outland Living Mega Fire Pit** is a good fit if convenience matters more than romance. Propane starts fast, stays predictable, and gives you a tidy setup that is easier to manage on decks, patios, and exposed corners.

## Best budget entry

**Amazon Basics Steel Lattice Fire Pit** is worth a look if your goal is simple affordability. Budget pits can work, but they make more sense in sheltered areas and for buyers who are realistic about longevity and cleanup.

## What actually works in wind

### 1. Better placement beats a bigger fire
Put the pit where fencing, a privacy wall, a shed, or the house itself breaks prevailing wind. A mediocre pit in a smart location beats a premium pit in the worst corner of the yard.

### 2. Low-maintenance fuel matters
If you use your backyard often, propane gets used more because it is easier. Many people buy wood for the experience and then end up using it less than expected.

### 3. Seating layout matters
Do not surround a windy fire pit evenly just because the furniture set looks symmetrical. Create a favored side with better chairs, side tables, and blankets where people actually want to sit.

## Best use cases

### Choose a smokeless wood pit if:
- You want a real fire experience.
- You are willing to manage fuel and ash.
- You can place the pit in a relatively protected area.

### Choose propane if:
- You want simple weeknight use.
- You care about clean patios and fast shutdown.
- Your yard is windy enough that smoke would be frustrating.

## Final recommendation

For an exposed backyard, propane is the safer recommendation for most people. For a more sheltered yard where the experience matters, a smokeless wood pit is the better long-term buy. If budget is the main driver, start lower-cost, but be honest that wind will expose weak designs fast.

## Recommended products

- **Solo Stove Bonfire 2.0** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_1)
- **Outland Living Mega Fire Pit** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_2)
- **Amazon Basics Steel Lattice Fire Pit** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_3)
'''
    },
    {
        'slug':'propane-vs-wood-fire-pit','title':'Propane vs Wood Fire Pits','category':'Fire Pits','deck':'A simple buyer’s guide for choosing the right fire pit fuel type based on maintenance, ambiance, convenience, and backyard conditions.','readTime':'7 min read','featured':False,
        'body': '''
# Propane vs Wood Fire Pits

This is the decision that shapes everything else. Size, style, and price all matter, but fuel type matters first. If you choose the wrong one for the way you actually live, the fire pit will not get used nearly as much as you think.

## Why people choose propane

Propane is easier. That is the whole case in one sentence. You turn it on, enjoy it, and turn it off. There is no ash, no hauling firewood, no smoky clothes, and less cleanup afterward.

Propane is usually the better fit when:
- the yard is exposed and windy
- you want frequent weeknight use
- the pit is part of a patio furniture setup
- you want a cleaner look

## Why people choose wood

Wood wins on atmosphere. The crackle, smell, and changing flame pattern are hard to replace. If your mental picture of a backyard fire includes roasting, tending the fire, and stretching the evening outdoors, wood still delivers the stronger experience.

Wood is usually the better fit when:
- you want a traditional campfire feel
- you have room for safe placement
- you do not mind ash and cleanup
- you use the fire pit as an event, not just a heat source

## Where people misjudge the choice

Many buyers think they want wood when what they really want is occasional ambiance without effort. That buyer usually ends up happier with propane.

Other buyers think propane will feel sterile, but if the goal is an inviting seating zone that gets used often, propane can be the smarter purchase because it removes friction.

## Cost and maintenance

Wood pits can have a lower entry price, but they bring ongoing work: wood storage, cleaning, ash disposal, and more careful siting. Propane tables can cost more upfront, but the convenience is real.

## Best picks by buyer type

### Choose propane if you are:
- busy
- likely to use the fire pit often
- building around a furnished patio
- tired of smoke and cleanup

### Choose wood if you are:
- after the full fire experience
- comfortable with more maintenance
- able to place the pit in a safer, more sheltered zone

## Final recommendation

For most homeowners building a polished, easy-to-use backyard, propane is the better practical recommendation. For people who genuinely want the ritual and feel of a real fire, wood is still the better emotional choice. The right answer is not which one is better in theory. It is which one you will actually use.

## Recommended products

- **Outland Living Mega Fire Pit** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_1)
- **Solo Stove Bonfire 2.0** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_2)
- **Fire Pit Cover 30 Inch Round** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_3)
'''
    },
    {
        'slug':'raised-garden-beds-canada','title':'Best Raised Garden Beds for Cold Climates','category':'Gardening','deck':'Raised bed options and planning tips for shorter seasons, colder soil, and weather that punishes cheap materials.','readTime':'8 min read','featured':True,
        'body': '''
# Best Raised Garden Beds for Cold Climates

Raised beds are one of the easiest upgrades for Canadian backyard gardeners. They warm faster in spring, drain better during wet weather, and make it easier to control soil quality. But cold climates punish flimsy beds fast, so durability matters.

## What to look for in a cold-climate bed

The best raised bed is not automatically the deepest or the cheapest. In colder regions, I would prioritize:

- structure that holds shape over time
- materials that tolerate wet soil and freeze-thaw cycles
- enough depth for roots and amended soil
- easy access for covers or hoops in shoulder season

## Best low-maintenance option

**Keter Maple Raised Garden Bed** is a good fit for people who want a cleaner, low-maintenance setup. Resin beds avoid some of the rot and upkeep issues people worry about with wood, while still looking more polished than a basic metal trough.

## Best value workhorse

A **galvanized steel raised garden bed** is often the best value option for cold climates. They are common, widely available, and well suited to vegetable gardening. The right one gives you a lot of planting volume for the money.

## Best add-on for season extension

**Garden bed cover hoops and mesh** matter more in cold climates than many new gardeners expect. If you can add frost cloth, insect mesh, or a simple low tunnel, the raised bed becomes much more productive.

## What depth actually makes sense

For herbs, greens, radishes, and many shallow-rooted crops, you do not need a giant bed. For tomatoes, carrots, and mixed vegetable planting, extra depth helps. Bigger is not automatically better if filling the bed properly blows the budget.

## Material tradeoffs

### Resin
Low maintenance and clean-looking, with good weather resistance.

### Galvanized steel
Great value, durable, and widely available.

### Wood
Looks natural, but quality and longevity vary a lot.

## Final recommendation

If you want a polished, easy-care setup, go with a resin or composite-style bed. If you want the most garden space for the money, galvanized steel is hard to beat. Then spend part of the budget on good soil and a basic cover system, because those two things often matter more than the bed itself.

## Recommended products

- **Keter Maple Raised Garden Bed** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_1)
- **Galvanized Steel Raised Garden Bed** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_2)
- **Garden Bed Cover Hoops and Mesh** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_3)
'''
    },
    {
        'slug':'beginner-garden-setup','title':'Beginner Backyard Garden Setup','category':'Gardening','deck':'A first garden plan that is realistic for busy homeowners and easier to maintain through the whole season.','readTime':'8 min read','featured':False,
        'body': '''
# Beginner Backyard Garden Setup

A beginner garden fails most often for one reason: it is too ambitious. Too many crops, too much square footage, too many containers, and not enough time. The best first setup is small, repeatable, and easy to water.

## Start with one manageable bed

One raised bed is enough to learn spacing, watering, soil improvement, and pest pressure. That is a win. You do not need a full backyard farm to get value from gardening.

## Good first crops

The easiest beginners crops are usually:
- lettuce and salad greens
- radishes
- green onions
- bush beans
- herbs
- one or two tomato plants

These give quick feedback and keep motivation high.

## The best starter equipment

**Keter Maple Raised Garden Bed** or another simple raised bed gives structure and limits sprawl.

**Seed starter trays with humidity dome** help you get ahead of a short season, especially if you want tomatoes, peppers, or herbs.

A **garden hose timer** is one of the smartest “boring” purchases because consistency is what beginners struggle with most.

## Soil is the real project

The frame matters, but the soil matters more. A new bed filled with weak, compacted material will disappoint no matter how good the bed looks. Put more money into good soil than beginners think they need.

## Keep the layout simple

One bed near a hose is better than two beds at the far end of the yard. Convenience drives consistency.

## Final recommendation

If you are new, build one bed, plant a short list of easy crops, automate watering as much as possible, and accept that learning the rhythm matters more than maximizing yield in year one.

## Recommended products

- **Keter Maple Raised Garden Bed** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_1)
- **Seed Starter Trays with Humidity Dome** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_2)
- **Garden Hose Timer** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_3)
'''
    },
    {
        'slug':'smart-backyard-setup','title':'Smart Backyard Setup','category':'Smart Backyard','deck':'The practical smart-home upgrades that actually make an outdoor space easier to use instead of just more complicated.','readTime':'8 min read','featured':True,
        'body': '''
# Smart Backyard Setup

A smart backyard should reduce friction. That means fewer manual steps, faster setup at night, easier security checks, and less forgetting to turn things off. If the gear adds complexity without saving time, it is not an upgrade.

## Start with the easiest win: plugs

Smart plugs are the fastest path to outdoor automation because they let you control ordinary devices without rebuilding the whole yard. Backyard lighting, seasonal décor, fountain pumps, and small accent features all become easier once they run on schedules or voice commands.

## Best for indoor-controlled backyard devices

**Amazon Smart Plug** is a strong fit when the device itself stays indoors or in a protected area and you want dead-simple Alexa setup.

## Best for exterior automation

**Amazon Basics Outdoor Smart Plug** makes more sense when the plug point is outdoors and exposed to weather. This is the one to look at for patio lights, holiday lighting, and other exterior circuits.

## Best camera-style add-on

**TP-Link Tapo C500 Outdoor Camera** is useful when you want flexible visual coverage of a yard, side path, or gate area.

## The best smart backyard stack for most homes

1. One smart plug for your main lighting zone.
2. One outdoor smart plug for exterior devices.
3. One camera covering the entry or side yard.
4. Routines that turn lights on at sunset and off at bedtime.

That is enough for most homes. Beyond that, complexity rises quickly.

## Final recommendation

Start with automation that you will notice every day: lights on schedule, easier night use, and quick control from Alexa. Add cameras or more advanced gear after that. The smartest yard is usually the one with the fewest moving parts.

## Recommended products

- **Amazon Smart Plug** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_1)
- **Amazon Basics Outdoor Smart Plug** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_2)
- **TP-Link Tapo C500 Outdoor Camera** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_3)
'''
    },
    {
        'slug':'automate-backyard-lighting','title':'Automate Backyard Lighting','category':'Smart Backyard','deck':'A simple path to lighting routines that make the yard feel finished every evening without extra effort.','readTime':'7 min read','featured':False,
        'body': '''
# Automate Backyard Lighting

Backyard lighting automation should do three things well: come on when you want it, shut off when you forget, and stay simple enough that the household actually uses it.

## The easiest starting point

Plug-in lighting is the easiest to automate. String lights, lanterns, café lights, and small plug-in features all work well because the smart layer sits between the outlet and the device.

## Best outdoor control option

**Amazon Basics Outdoor Smart Plug** is the cleanest starting point for exterior lighting. It makes timed schedules and Alexa control straightforward without adding a full smart-home hub.

## Best indoor protected option

**Amazon Smart Plug** is ideal when the plug stays in a dry indoor or sheltered location and you are running lights that feed outdoors from there.

## When smart lights themselves are worth it

If you want scenes, app color control, or zone-based ambiance, **smart LED outdoor string lights** can be worth the upgrade. For most people, though, a regular light set plus a smart plug is the cheaper and simpler choice.

## Good automation routines

- Sunset on, midnight off.
- Sunset on, 30% dim after 10 p.m. if your setup supports it.
- Vacation mode that randomizes on/off timing slightly.
- Voice routine for “backyard on” and “backyard off.”

## Final recommendation

Automate the lights you already use most often, then stop. A yard with one reliable routine feels better than a yard with ten half-finished automations nobody remembers how to manage.

## Recommended products

- **Amazon Basics Outdoor Smart Plug** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_1)
- **Amazon Smart Plug** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_2)
- **Smart LED Outdoor String Lights** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_3)
'''
    },
    {
        'slug':'cozy-backyard-setup','title':'Cozy Backyard Setup','category':'Comfort','deck':'How to make a backyard feel warmer, softer, and more inviting without overfilling it with décor.','readTime':'7 min read','featured':False,
        'body': '''
# Cozy Backyard Setup

Cozy outdoor spaces are not built with clutter. They are built with three layers: warm light, comfortable seating, and just enough heat or softness to extend the evening.

## Start with lighting

The easiest way to make a backyard feel more inviting is to lower the visual harshness after dark. Overhead or perimeter string lighting does this fast.

**Addlon 48FT Outdoor String Lights** are a strong anchor because they create atmosphere without needing a full redesign.

## Add comfort you will actually use

An **outdoor throw blanket with a waterproof backing** is one of those simple upgrades that gets used more than decorative pillows. It is practical, stores easily, and helps during cool shoulder-season evenings.

## Add heat only if the space needs it

A **portable propane patio heater** works when you want warmth but a fire pit is not practical, permitted, or convenient.

## The cozy layout formula

- One soft lighting layer.
- Two to four seats that face each other naturally.
- One side surface for drinks.
- One warmth layer, either blanket or heater.

That is enough for most patios.

## Final recommendation

Make the yard comfortable before making it decorative. Light, seating, and warmth beat filler items every time.

## Recommended products

- **Addlon 48FT Outdoor String Lights** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_1)
- **Outdoor Throw Blanket, Waterproof Backed** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_2)
- **Portable Propane Patio Heater** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_3)
'''
    },
    {
        'slug':'small-backyard-transformation','title':'Small Backyard Transformation','category':'Comfort','deck':'Small-space upgrades that create more function and better visual impact without making the yard feel crowded.','readTime':'8 min read','featured':True,
        'body': '''
# Small Backyard Transformation

A small backyard does not need more stuff. It needs clearer priorities. The best transformations happen when every addition earns its footprint.

## Focus on three jobs

In a small yard, try to make every upgrade support one of these:
- seating
n- storage
- vertical or edge-based visual impact

## Best compact garden add-on

A **Keter raised planter box** or similar elevated planter adds greenery without consuming the whole yard.

## Best dual-purpose furniture move

An **outdoor storage bench deck box** gives you seating and hidden storage at the same time. That is exactly the kind of overlap small spaces need.

## Best visual upgrade per square foot

**Addlon 48FT Outdoor String Lights** or another perimeter light run adds height, mood, and definition without taking floor space.

## The small-yard rule

Do not fill the middle if you can improve the edges. Lighting, planting, storage, and vertical definition around the perimeter usually make a small backyard feel larger and more complete.

## Final recommendation

Prioritize one seating zone, one hidden-storage solution, and one overhead or perimeter lighting layer. That is the fastest route to a small backyard that feels designed instead of crowded.

## Recommended products

- **Keter Raised Planter Box** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_1)
- **Outdoor Storage Bench Deck Box** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_2)
- **Addlon 48FT Outdoor String Lights** — Affiliate link: [Shop on Amazon.ca](PRODUCT_LINK_3)
'''
    },
]

# fix typo in one body
for a in articles:
    a['body'] = a['body'].replace('\nn- storage', '\n- storage')

product_map = {}
for slug, name, ptype, note, link in products:
    product_map.setdefault(slug, []).append({'name': name, 'type': ptype, 'note': note, 'link': link})

# write articles with injected links
for art in articles:
    body = art['body']
    plist = product_map[art['slug']]
    for idx, p in enumerate(plist, 1):
        body = body.replace(f'PRODUCT_LINK_{idx}', p['link'])
    # YAML front matter
    fm = {
        'title': art['title'],
        'slug': art['slug'],
        'category': art['category'],
        'description': art['deck'],
        'readTime': art['readTime'],
        'featured': str(art['featured']).lower(),
        'metaTitle': art['title'] + ' | Backyard Upgrades',
        'metaDescription': art['deck'],
    }
    front = '---\n' + '\n'.join(f'{k}: "{v}"' for k,v in fm.items()) + '\n---\n\n'
    (articles_dir / f"{art['slug']}.md").write_text(front + textwrap.dedent(body).strip() + '\n', encoding='utf-8')

# write articles manifest
manifest = [
    {
        'slug': a['slug'],
        'title': a['title'],
        'category': a['category'],
        'featured': a['featured'],
        'readTime': a['readTime'],
        'deck': a['deck'],
        'description': a['deck'],
        'metaTitle': a['title'] + ' | Backyard Upgrades',
        'metaDescription': a['deck']
    }
    for a in articles
]
(data_dir / 'articles.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')

# products csv
with (data_dir / 'article_product_map.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['article_slug','product_name','product_type','selection_note','affiliate_url','link_type'])
    for slug, name, ptype, note, link in products:
        writer.writerow([slug, name, ptype, note, link, 'direct_product' if '/dp/' in link else 'search_link'])

# legal/support pages
pages = {
    'about.md': '''
# About Backyard Upgrades

Backyard Upgrades is a practical outdoor-living site built for homeowners who want a better backyard without wasting money on the wrong products or overcomplicated ideas.

The focus is simple:

- practical upgrades over flashy trends
- real-world product picks over filler lists
- guidance that helps you make progress with the space you already have

Most backyard projects fail for one of two reasons: people either overbuy before they have a plan, or they overdesign before they understand how they will actually use the space. This site is built to avoid both mistakes.

## What you can expect

You will find articles on backyard lighting, fire pits, raised garden beds, comfort upgrades, and simple smart-home additions that make outdoor spaces easier to use.

The tone here is intentional. The goal is to be useful, not noisy.
''',
    'affiliate-disclosure.md': '''
# Affiliate Disclosure

Backyard Upgrades participates in affiliate advertising programs, including the Amazon Associates program. That means this site may earn a commission when you click certain product links and make a purchase, at no additional cost to you.

## What that means for readers

- Product links may be affiliate links.
- A commission may be earned if you purchase through those links.
- Editorial intent is to recommend products that fit the article topic and buyer use case.

Affiliate relationships do not change the price you pay. They do help support the ongoing operation of the site.
''',
    'privacy.md': '''
# Privacy Policy

Backyard Upgrades values your privacy.

## Information collected

This site may collect limited technical information through standard website hosting, analytics, or form tools if those are added later. That can include browser type, device information, referring pages, and general usage information.

## Affiliate links

This site contains affiliate links. Third-party retailers may use cookies or tracking technologies to attribute purchases.

## Contact

If you need to request updates or removal of submitted contact information, use the site contact page or listed email address.
''',
    'contact.md': '''
# Contact

Questions, partnership inquiries, or site feedback can be directed through the site contact page or by email once the publishing setup is finalized.

For launch, add one clear contact email and reuse the site design system for a simple static contact page.
'''
}
for name, content in pages.items():
    (legal_dir / name).write_text(textwrap.dedent(content).strip() + '\n', encoding='utf-8')

# handoff docs
(docs_dir / 'PUBLISH_READY_HANDOFF.md').write_text(textwrap.dedent('''
# Backyard Upgrades Publish-Ready Handoff

This package is designed to help Codex or a developer take the current Backyard Upgrades project from draft status to launch-ready status.

## Included in this package

- 10 rewritten publish-ready article markdown files
- Enriched `articles.json` metadata file
- Product mapping CSV with affiliate-tagged Amazon Canada URLs
- Draft legal/trust page copy
- Launch checklist and implementation notes

## Important note on affiliate links

The product map includes two affiliate URL types:

1. `direct_product` — exact Amazon Canada product pages where a retrievable product URL was available.
2. `search_link` — Amazon Canada affiliate-tagged search URLs where the exact Canada product page could not be verified cleanly from the browsing environment.

Search links are usable for handoff and staging, but exact product-page replacements should be made during final QA where possible.

## Required Codex tasks

1. Replace existing article markdown files with the versions in `content/articles/`.
2. Merge the supplied `data/articles.json` fields into the live `content/articles.json`.
3. Replace affiliate placeholders with product callout blocks using `data/article_product_map.csv`.
4. Add supporting pages:
   - about
   - affiliate disclosure
   - privacy
   - contact
5. Add `robots.txt` and `sitemap.xml`.
6. Check all article slugs and internal links.
7. Confirm relative paths work for GitHub Pages.

## Suggested article callout pattern

Use a clean card block with:
- product name
- 1-sentence why-it-fits note
- button label such as “Check price on Amazon”
- disclosure line near the CTA or in page chrome

## Minimum launch QA

- no placeholder affiliate links remain
- article filenames match metadata slugs
- legal pages are linked in header or footer
- homepage cards show clean decks/excerpts
- pages load from static hosting with no build step
- search and filters still work
''').strip() + '\n', encoding='utf-8')

(docs_dir / 'LAUNCH_CHECKLIST.md').write_text(textwrap.dedent('''
# Launch Checklist

## Content
- [ ] Replace first-pass article drafts with final markdown files from this package
- [ ] Add internal links between related articles
- [ ] Confirm product callouts render consistently

## Trust and compliance
- [ ] Publish affiliate disclosure page
- [ ] Publish privacy page
- [ ] Publish about page
- [ ] Add contact route or email

## Technical
- [ ] Add robots.txt
- [ ] Add sitemap.xml
- [ ] Add favicon assets
- [ ] Confirm GitHub Pages path behavior
- [ ] Test homepage filters and article pages

## Affiliate QA
- [ ] Verify each direct Amazon link resolves
- [ ] Replace search-link placeholders with exact product URLs where possible
- [ ] Confirm affiliate tag is present on every Amazon URL
''').strip() + '\n', encoding='utf-8')

# zip
zip_path = Path('/mnt/data/backyard_publish_handoff.zip')
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for path in root.rglob('*'):
        if path.is_file():
            z.write(path, path.relative_to(root.parent))

print(f'Wrote package to {zip_path}')
