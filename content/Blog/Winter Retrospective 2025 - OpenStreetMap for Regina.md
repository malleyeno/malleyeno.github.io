---
{"publish":true,"created":"2025-10-15","modified":"2025-12-16","published":"2025-12-17","tags":["Regina","OpenStreetMap","post","geography"],"cssclasses":"","socialImage":"https://malleyeno.com/Blog/attachments/winter2025ReginaOSMRetro.png","socialDescription":"Now that the snow has fallen, I decided to reflect on contributions I made to Regina's OpenStreetMap."}
---

![[Blog/attachments/winter2025ReginaOSMRetro.png|Banner image of Malle writing in a notepad in the foreground, the map of Regina in the background in the Transport layer mode with attribution in the bottom right. Regina OpenStreetMap Winter 2025 Retrospective is superimposed.]]
*Alternative titles considered: OSM Wrapped, Recap Regina, OpenStreetRecap — all rejected for being a bigger stretch than the categories I got from Youtube Music for my year’s listening*

The snow’s here! Since I’ll be couped up inside a lot more than I normally am (so like… 5% more I guess), I figured now is the time to recap my contributions to OpenStreetMap this past year. Since the vast majority of my work is in Regina, Saskatchewan, I’ll just focus on that. (Besides, the KW OSM[^1] community scares me a little. They *respond* to map notes out there. *shiver*)
# StreetComplete Surveying
We don’t get a lot of warm weather up here, so getting out while I could to do some surveying was a large part of my contributions. The vast majority of my edits came from [SCEE](https://github.com/Helium314/SCEE) (the advanced [StreetComplete](https://streetcomplete.app/)), which is probably the best way to enrich OSM data on the ground if you haven’t lost enough sanity to use Vespucci. 

> [!figure] ![[Blog/attachments/2025-sceestats.png|A screenshot of my SCEE profile with stats. Overall, I had 69696 contributions, ranked 2 in Canada, 96 globally, had 349 days active, and had 586 achievement levels.]]
> That contribution number makes me go "Niceniceni". I'll check back after about 627,273 more contributions.

Since I met [someone who actually uses building data](https://nafithebear.phenjara.de/) (side note: [I met two people now!](https://pronghornmaps.com/)), those surveys focused on building attributes. Levels, roofing types, colours, colours of roofs, we got ‘em! [We have a little 3D model of the north-end going!](https://demo.f4map.com/#lat=50.4919565&lon=-104.6377137&zoom=16)

> [!figure] ![[Blog/attachments/2025-f43Dmap.png|A screenshot of Regina North End as seen on F4map's 3d model viewer.]]
> Who needs drones when you have eyeballs? (Actually a drone would be really useful 👉👈)

Accessibility attrs were another focus for me. Widths, surface conditions and material, and lighting were some of the most common attrs for ways I added. Crossing attributes will come up next, but those will depend on [[Blog/Winter Retrospective 2025 - OpenStreetMap for Regina#Separate Sidewalk Mapping]] before I can really go ham on them.

> [!figure] ![[Blog/attachments/2025-RochdalePasquaCrossing.png|A screenshot of Regina's Rochdale/Pasqua crossing, as mapped in iD. Several separately mapped sidewalks, curb nodes, and intersection nodes are mapped.]]
> Behold: the eternal intersection!

(Special mention to [EveryDoor](https://every-door.app/) for allowing mapping entry points without knowing an address. That’s been pretty useful for unmarked doors that I’ve seen people go in. Plus entry nodes are the only way I know of mapping the width of doorways — [something I’ve been told is the next big advance to make in accessible mapping](https://www.openstreetmap.org/user/Malle_Yeno/diary/406833#comment59341).)

# Street-Level Imagery Collection
I got a GoPro Max this year! Regina has low coverage of street-level imagery when you look at [Mapillary](https://www.mapillary.com/app). The results are different for KartaView, but the interface is also worse and the performance is terrible for uploading. My contributions are filling more of the north-end with 360 street imagery, and hopefully by next snowfall I can fill that out.

I may request ideas for where else to explicitly go collect imagery for, [like this user did for Montreal.](https://community.openstreetmap.org/t/choosing-areas-to-prioritize-for-street-level-imagery-in-montreal-en-choisissant-les-lieux-a-prioriser-pour-les-photos-aux-niveau-de-la-rue-a-montreal/108895) Might not get a ton of bite with Regina’s lower and quieter user base, but maybe the chicken needs to lay the egg before the egg decides to use OSM data.

One issue that’s bothered me is choice of provider. With how all these tech companies are using the data they have to support inhumane policies, this will be something I think about more before I continue going hard in contributing to a company that works under the Facebook umbrella. I’d love to use [panoramax](https://panoramax.fr/), but so far it looks like the main instance is for France (and while they allow worldwide imagery, they openly state they don’t have appropriate infrastructure for that to scale.) I gave thought to hosting my own panoramax instance for just Regina (or the Prairies), but I simply don’t have the experience with hosting to do that confidently. 
# Separate Sidewalk Mapping
There are two approaches to mapping sidewalks in OSM: as attrs on a way, and as separate ways entirely. The latest Pedestrian Working Group schema recommends the latter and not the former for reasons they elaborate better than I can, mainly focused on accessibility.

Regina sidewalks have been mapped predominantly as attrs on ways (thanks to the steadfast work of contributors such as [gecho111](https://www.openstreetmap.org/user/gecho111)). After checking with them on [whether we should move to the separate sidewalks method](https://www.openstreetmap.org/user/gecho111/diary/398031), I have begun that work. So far, areas in the north-end are making progress. The east-end Costco (future proofing this article by specifying that~) also has separate footpaths, since I micromapped[^2] that area. To coordinate my progress, I made a personal project in [SimpleTaskManager](https://stm.hauke-stieler.de/) where I can map each part of Regina in little squares. Based on that, it looks like I’m about... 3% done.
> [!figure] ![[Blog/attachments/2025-SidewalksProject.png|A screenshot of a SimpleTaskManager for a project called "Sidewalks Regina". A large grid layer is over a map of Regina, with majority grids being red with some green in the north and east. The progress bar at the top shows 3%.]]
> Slow and steady 🦝💦

With winter shutting down any real surveying attempts on my end, I expect sidewalk mapping to take more of my OSM effort these next few months (assuming I find the time for contributions!)

# Indoor Mapping
A lot of OSM focuses on mapping the outdoor environment as easily visible from aerial images. But what I’m really hoping might catch on is indoor mapping. That’s where you make a map of the inside of a building. 

My usual source for this information are the fire evacuation maps for said buildings. Using that, I’ve managed to [complete an indoor map of the Central Branch of the Regina Public Library](https://indoorequal.org/#map=19.11/50.4485282/-104.6143685&level=0). No small task since it’s three levels and has a bajillion rooms, plus an elevator that according to the map teleports locations between floors. This was an interesting thing to [stream on Twitch](https://www.twitch.tv/malle_yeno)!

> [!figure] ![[Blog/attachments/2025-indoorRPL.png|A screenshot from IndoorEqual of the base floor of the central branch of Regina Public Library. The rooms are visible within the building outline.]]
> Not pictured: the elevator that moves you five meters to the left if you go up.

Fingers crossed that I can get my paws on some other fire evac maps to do some other buildings. Even directory maps could be useful. I have my eye on you, Cornwall Centre. And speaking of…

# Updates to Cornwall Centre
I’m real happy about how many updates I made to the Cornwall Centre. And apparently, so are some of y’all! I received a kind kudos in my OSM private messages from someone visiting this year from the US! 

> [!figure]  ![[Blog/attachments/2025-cornwallThanks.png|OSM DM dated July 2025 reading "Hiiiiiii! I came to Regina on vacation from the states and noticed that you’ve done a great job mapping Cornwall Centre. Nice work!" The sender username, ending name, and exact date and time are redacted for privacy of sender.]]
> How sweet 💚

Lots has changed in Regina this past year, especially in the retail space. Every time I went to Cornwall, something needed to be changed. Stores moved, shops closed, new pop-up shops came out. I think I was pretty on top of the changes in there.
# Wiki Work
I didn’t contribute much to the [OSM Wiki](https://wiki.openstreetmap.org/wiki/Main_Page) community before, but this year I took a stab at it.
## Updates to Regina wiki page
Probably the bulk of my edits went to the [Regina Wiki Page on OSM](https://wiki.openstreetmap.org/wiki/Regina). I didn’t make it from scratch, but it was more than a little out of date. The topics on there were still talking about getting street names of the city into the map (a problem which seemingly has been solved for everything short of new developments). I decided to revamp the page to discuss new opportunities, considerations, and background on Regina. Now, I think the page can act as a hub for the enterprising contributor to see what kind of work they can hop into around here. 

It might be a bit *too* intimidating for a new contributor. There’s a lot of detail I tried to put in. I might need to cut it back a bit and have it be an easier thing to digest. But it’s here now and that’s better than the alternative.
## Creation of Regina Transit wiki page
Regina Transit is the city’s only bus transit system. Our routes are… let’s say, something that will get you acquainted with working in OSM *real fast*. Having a route with the same number that has *four* variations is a case study in something but I don’t know what.

I created a [wiki page for Regina Transit](https://wiki.openstreetmap.org/wiki/Regina_Transit) to document the routes within the city. And by doing that, I discovered “hey, we’re missing some.”
> [!figure] ![[Blog/attachments/2025-reginaTransit.png|A screenshot of the table on the Regina Transit wiki page. All entries have links to route relations, except for Route 24 Airport/Cornwall Centre.]]
> Looks like we got a new project in the queue!
## Proposal for `bicycle_parking=no`
While surveying around the north-end, I noticed a bunch of places that don’t have anywhere to park your bicycle. In OSM, you don’t normally map the negative case (“there’s nothing here”). You map what’s on the ground, not what’s *not* on the ground. But this felt like an exception. After all, isn’t it important to know that a place actually lacks bicycle parking, rather than someone might just not have mapped that parking yet?

When I asked this in the OSMUS[^3] slack, it appears I wasn’t alone in those thoughts. But right now, there isn’t a documented way of showing that a place specifically lacks parking for bikes. I hope to change that with [my proposal to allow bicycle_parking=no](https://wiki.openstreetmap.org/wiki/Proposal:Bicycle_parking%3Dno_on_not_amenity%3Dbicycle_parking_to_indicate_absence) as an attr. 

The proposal is taking me a while to draft because I’m trying to be thorough. But it’s almost ready for comments!

# Conclusion
What a year!

Lots of work happened in OSM this time around. I think there will be more to come next year, especially as sidewalk geometry gets mapped. Aerial imagery helps get the geometry just *there*, but the ideal state is that the attrs on those sidewalks get mapped too. And a lot of that needs to be surveyed. No small task, but it’s gotten started and it'll keep moving.

[^1]: By the way, I’m going to be using some shortforms and jargony words throughout this post. *OSM* means *OpenStreetMap* and *KW* is Kitchener-Waterloo. *Attrs* means *Attributes* (or what OSM calls “tags”, but since I work in geography, I call those attrs by habit). *Ways* are line features in OSM. *Areas* are technically ways in OSM too, but calling them areas makes it clear that they are closed shapes and not just lines (or as we say in the biz, they’re polygons.) If I missed one, let me know and I’ll update this bit.

[^2]: Micromapping means making a really detailed map for an area in OSM.

[^3]: OpenStreetMap United States (a group focused on american contributions to OSM, but with enough footprint to be a sort of gathering ground.)
