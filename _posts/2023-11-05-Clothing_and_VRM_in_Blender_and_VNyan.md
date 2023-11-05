---
title: Clothing and VRM with Blender and VNyan
---
Getting clothing to work on VRM models is a bit tricky. But we discovered a way to make toggleable clothes [while I was streaming updates to my model over on Twitch!](https://www.twitch.tv/malle_yeno) We discovered a way to customize your VRM in Blender to have clothes, and them turn them on/off in VNyan. These are my rough notes on how to make this happen. I might refine this more in the future!

## In Blender
- [Use blender vrm plugin](https://vrm-addon-for-blender.info/en/)
- Skipping all the parts where you set up your VRM until you have to assign shapekeys.
- Make individual meshes for each clothing item and set them up as you would.

![](/assets/images/blender_XA0mkW1PE8.png)

Notice here that each shirt is its own mesh, even though I have each mesh exactly the same. Each one of them needs to be visible and will be on your model. 
- the issue: you need to make a material transparent to turn off clothing. But material shape keys are tricky in blender.
	- The answer: don't use them in blender! We are going to use the VRM plugin to alter material values for us, and have another program call each of them instead.
- Make each clothing item use their own material. Keep the material name the same as the mesh for your own sake of memory.

![](/assets/images/blender_eJecBvTEWw.gif)

I am clicking through each mesh here to illustrate they each have their own material with a new design on them.
- Make a blendshape in the VRM side menu for each clothing item. Do not use a preset, but assign names you're likely to recall as being relevant to your clothing.

![](/assets/images/blender_zoGPVLCscp.png)

Note that I havent named them similar to the mesh or material. You can do so if it helps your memory, but we will need these names specifically when we go to vnyan, so don't make them complicated to type or remember.
- Under options, set Is Binary to true, and expand the Material Values

![](/assets/images/blender_MDWiLe9hMz.png)

- Next to Material, pick the relevant material to your clothing item. 

Flexx_Shirt.003 is my "excuse me" shirt design, so that is why it is under that blendshape.

- Next to Property Name, type \_Color
	- **You must spell it this way exactly**. Underscore, title cased, and in american spelling. If you experience errors, triple check your formatting here.

![](/assets/images/blender_5Oxmyj5RVE.png)

- Add four value slots and set them all to 0. Confusingly, 0 means visible for VRM. Setting them to 100 means invisible. You'll need to know this when we go to VRM. 

![](/assets/images/blender_unJrG3EJbV.png)

(No, you cannot do middle values to get partial transparency. We turned "is Binary" on for a reason: VRM has trouble handling alpha values. If you find a way to do partial transparency, I'd love to hear your method.)
- Export your VRM

## In Vnyan
- have a node graph dedicated to clothing
- On application start, set your tracker variable for if you will get clothing in the next trigger or not (not *which* clothing, just the presence of clothing. You might not need this if you never plan to have 0 of your accessories on at any given moment.)

![](/assets/images/VNyan_vFvROilfoT.png)

- For your redeem, set something to check the value on that variable

![](/assets/images/VNyan_2WnTmm69EN.png)

- when its time to not have a shirt, set all your blendshapes to 100 and also set your clothing toggle variable. You can also have addition effects when you are naked, like a sound effect
	- If you would want to swap clothing without having a "naked" toggle, you must make one anyway because you have to reset all your clothing before applying new ones. Otherwise, you will layer them together on each new clothing item and likely start clipping.

![](/assets/images/VNyan_lmwktf7wsF.png)

- For each clothing item you'd like to be turned on, have a trigger that turns that blendshape to 0

![](/assets/images/VNyan_NWeMsnR3a6.png)

- Call that trigger in any way you so choose. If you'd like to pick it randomly, consider my setup (see how the "pantsOn" trigger is activated on 1 and 5. All outputs of Random 10 must be allocated since empty outputs are pickable and will lead to nothing happening
	- Notice that "shirt_time" is always called when any shirt is applied. This is important for a toggle on each redeem.
    
![](/assets/images/VNyan_wjC0LTstiu.png)
