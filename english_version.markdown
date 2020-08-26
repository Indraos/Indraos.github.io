---
layout: post
title:  "Data, Corona Hotspots and Structural Violence"
date:   2020-08-26 08:00:00 +0100
categories: decide
---
The COVID-19 pandemic required and requires coordinated and strong cuts in our mobility. In addition to individual people who have a major influence on the spread of a disease, the focus is also on places, so-called "hotspots". In theory, extensive access to mobility data enables the effects of the closure of public spaces to be determined very precisely. I and my fellow researchers do just that. Despite major ethical challenges, we see ways in which the power of mobility data can be used for good.
<!--more-->
## Close hotspots instead of denouncing super spreaders
The passing on of infections to others is not evenly distributed. Pictures from the last few months often show people drunk spring breakers on crowded beaches, people demonstrating crowded, places of worship with a singing congregation of believers. People who have many such social contacts as sick people and those who do not adhere to rules, so-called super spreaders, or those who could be, play an important role in all of these examples.

In the last global pandemic, the Spanish flu, which reached Europe in the early summer of 1918 at the end of World War I, understanding of the disease was far from a level at which superspreaders could have been identified. Daily newspapers described the disease as "mysterious", "puzzling" or "unknown". Mass events were not restricted. In the final phase of the war, newspapers were also censored as a communication and documentation medium except for the war-relevant part.

![Kölner Lokalanzeiger 30.05.2018, public domain](/assets/img/covid_newspaper.png "A first mention of the Spanish flu in the Kölner Lokalanzeiger")

However, people are often wronged with the new concept of the superspreader. Because places where people work and love can also play an important role in who becomes super spreaders, and this is often not voluntary. The last few months have brought examples of places where, at least at times, people involuntarily come together in a confined space: people on cruise ships (Diamond Princess), butchers in slaughterhouses (Gütersloh), or stewards on flights - whether out of physical limitations or economic necessity . Here it is places rather than people that lead to contamination of people.

And whoever visits such places is not by chance. There are already socially disadvantaged people who have to use public transport or who cannot work from home. Many people who are in fact super spreaders are therefore often not only people who are forced to frequent more dangerous places, but are also often more at risk from the pandemic. It is therefore dangerous to treat super spreaders disparagingly without considering their individual situation.

The risk of meeting places can be assessed more objectively. According to the current state of knowledge, closed rooms with little air movement, whose normal use includes speaking, are places of high risk, regardless of their use, and potential hotspots of infection. All people who can come close together in such places should be infected, be super-spreaders.

A good example of the importance of places for infection is Mary Mallon from New York, who infected over 50 people with typhoid fever in the early 20th century. She worked as a cook, was a carrier of the disease, but showed no symptoms. She cared for people she infected, mostly at her different workplaces, and passed the disease on herself. Mrs. Mallon's risk of infection was influenced by places and their economic situation, more than personal choices.

As a result, capacity limits and closings of high risk locations have been some of the responses to COVID-19. Potential hotspots, such as restaurants, bars, and churches, were closed longer this spring and early summer. Such restrictions also allow individuals to worry less about how to adjust their behavior. You don't have to decide to turn down an invitation to church, for example, or refuse fellowship in order to receive fellowship in other ways. Closures and capacity constraints make it easier for people not to become super spreaders, even if they are not forced to do so by their physical or economic situation.

![Writing on Typhoid Mary, public domain](/assets/img/covid_typhoid_mary.jpg "A writing about the super spreader Mary Mallon.")

## Decide on data-driven closings

This suggests closing particularly dangerous places - and this is very possible with existing data.

In an ongoing project with researchers at the MIT Media Lab, we are using data to assess the risks of places in a more informed manner.

The first thing to note here is how amazingly data we are. For each of the approximately 40,000 postal codes in the United States, Safegraph offers weekly visitor numbers to approximately 6 million points of interest (which are supermarkets, but also churches). Safegraph receives this data from various smartphone apps, aggregates and de-anonymizes it. The rights of use and ownership of this data are in another chapter, which we do not turn to here.

But it doesn't stop with mobility data. It is also possible to determine the number of people in a location per hour and the floor space of buildings also exist, thus making it possible to estimate the likelihood of infection by two random people in one location. There are also average credit card bills, which show the economic activity of a place. (In America, the majority of people have a credit card.) Other studies have given a representative survey of which type of facility they would prefer over others if only one type can remain open (sample question: "Would you rather see churches or tobacco shops open?") . This makes it possible to assess how essential places are considered to be based on the likelihood of infection and economic significance. And the reaction of closings can also be understood with data. With data from pre-Corona times, a guess can be made as to how likely it is that people will drive to an ice cream parlor further away when a closer one closes, and how likely it is that they will not make visits.

Data scientists with a great deal of self-confidence can use this data to write down a major optimization problem for which places should remain open and which should remain closed. The fact that the data is rich enough to also estimate the behavior of people in the event of closings enables not only large and well-resolved, but also authentic models to be written.

![Mobility graph, PNAS, 2009](/assets/img/covid_mobility_graph.png "A mobility graph of the United States.")

Such a model, or at least a risk assessment that also includes people's reactions, is set up by my colleagues and I.

## Optimization of the ethical pillory

Many ethical challenges become opaque in such a model. Not only can such an optimization approach exacerbate social fragmentation and lead to final decisions that are probably not desired, it can also do this in a very intransparent manner. Before I try to save our research, here is a triad of ethical problems that arise when optimizing with large data.

The model can implicitly exacerbate segregation. For example, it is very natural for people to visit multiple points of interest during a COVID incubation period. If so, they can get infected on a first visit and pass the virus on a second. In order to prevent the virus from spreading, it would tend to be optimal to close points of interest that connect parts of the city (e.g. near bridges) so that people have less incentive to move to a different part of the city than their residential area. That sounds like a quarantine of entire city districts, enforced by mobility nudges, which, combined with different medical equipment and different health conditions of the population, cause unequal chances of survival in each district. The question must be: How are the negative effects of the closure regulation distributed? Are the people who are already in bad shape hit more than others?

Furthermore, this cannot give any compact justifications for closing decisions. Let us assume that the model calculates that a certain point of interest should optimally be closed. In this case, an affected person, such as one who cannot walk far to a supermarket because of a walking disability, may not be able to get a good explanation of why this decision is made. Because the model tries to map human behavior, its decisions are complicated, cryptic. It could answer that the risk of this supermarket is too high given the level of essentiality as determined by consulting the population. It is questionable whether this will satisfy the person concerned with the process. So we also have to ask ourselves: Is the process of being decided in such a way that people can interact with it and have an impact on the outcome for them?

After all, in such a model it is all too tempting to write certain value conflicts directly into the mathematical model instead of reflecting them.

## The justification of big data

The three reasons weigh heavily, here a defense of the data-driven research of COVID closings.

First, it is important to make it clear to people that visiting multiple locations in an incubation period, and thus the chance of being infected once and passing the disease on on a next visit, is a real possibility. This could then influence how the risk of places is assessed. Policy makers need an assessment of how relevant these effects are in order to make decisions based on them. But even individuals should see that the dangers of airplanes do not only come from bringing people together in a small space. It is also important that airplanes mix people from all possible locations, and people from a location with a low COVID prevalence are now exposed to the average group of air travelers. On the one hand, this can relax the way people deal with the place, on the other hand it can also influence the interaction with people. In this way, data-driven research can help shape the way people think. This article is already part of it.

Second, data-driven research is also important to justify pragmatic decisions. If the data shows that many smokers do not have cigarettes delivered to their home when the next cigarette shop closes, but rather drive as far as they want, then it probably makes little sense to close these shops because they will close only to a greater utilization of more distant cigarette shops, and a more heterogeneous visitor base. So if data actually shows that smokers travel far to buy cigarettes, staying open to cigarette shops can be justified, even from a COVID risk assessment.

Finally, working with data that spans an entire country can make the specifics of the environment transparent to local decision-makers. [Compilations] (https://www.uschamber.com/international-affairs-division/covid-dashboard) for the measures of different countries enable decision-makers to coordinate their regulations. Research that gives local authorities a clear idea about visiting patterns of places can enable regulations to be adapted locally. Evidence that we provide can put a local discussion on a foundation, and thus relieve the decision-makers in their decision-making pressure, for example when closing important places of economic activity.

We need a good understanding of human behavior to close really risky places. Data enables us to do this and gives us power and responsibility. However, the decision must still lie where the knowledge of local characteristics is: on site.