---
layout: post
title:  "Getting Back from the Pond: Improving the Ride-Hailing Market"
date:   2020-08-26 08:00:00 +0100
categories: decide
---
The summer comes to an end, but ponds can still remind us of almost forgotten mask-free times. For city-dwellers that don't own a car, getting to these distant natural monuments---and back---can be frustrating. When waiting for a Lyft for more than an hour, an afternoon at the pond can become an early-evening catastrophe.
Maybe, for all the minutes waiting, an Uber driver was close. But really, who would know that? [Only 9%](https://secondmeasure.com/rideshare-market-share/) of Americans that regularly use ride-hailing apps use more than one of them regularly.
<!--more-->
##Why not only one platform?
Waiting so long or being forced to look into different apps to find a ride sounds inefficient. An easy fix could be to let Google Maps show offers from all ride-hailing platforms at once. Maps then would intermediate between the customers and the ride-hailing outlets. Having one single app for ride-hailing would be very convenient for customers, and waiting time at ponds and elsewhere would be minimized.

Nevertheless, an intermediary Maps would put ride-hailing platforms at existential risk. Noone would have a reason to have Lyft's app installed if there was Maps. This unique access to consumers gives Google all bargaining power when negotiating terms of business with Lyft. Presenting offers to the consumer would make Maps the Boss of the Business. 
And also the drivers would be in a weak bargaining position. In the case that their working conditions or pay become unacceptable, there is no competitor they could work for.
Whether the benefits of a single intermediator in the ride-hailing market outweighs its drawbacks is hence uncertain. What is certain is that mandating a monopoly from above is a Herculean regulatory effort.
## Designing a System for Customer Exchange

Before we start implementing a questionable system with a single intermediator, we could look for more subtle forms of making the market more efficient. And in our pond example, another fix is imaginable. 

Let's assume that there was an Uber driver close-by during our hour of waiting. In this case, the Uber driver will be far away from the city, and most likely, would need to drive back without a customer. Being faced with the alternative of an empty car, Uber would be willing to pick us up almost for free. And Lyft, instead of letting us wait and serve us in an hour, would also be happy with much less money than we would be willing to pay for the ride. So Lyft could sell access to a customer to Uber.

## Challenges of Uncertainty

Before we finish, let's look at one intricacy when the case is not as straightforward as with us waiting at the pond. An Uber driver might be somewhat close by and better serve you, but neither Uber nor Lyft alone can know whether this is the case: They don't have access to the locations of each other’s drivers, and probably would not be willing to share this information. Hence, with little information, Uber must decide how much it would be worth to them to have an additional customer that requested a ride in another app. Similarly, Lyft must decide how much they would need to get reimbursed to forward a customer on their own app to their competitor.

Given Uber’s and Lyft’s uncertainty about where the other’s drivers are, even trades that would minimize waiting time and maximize time of drivers with a customer might not happen. The argument why Lyft should charge a bit more than their willingness to pay goes as follows: When Uber offers an amount for a consumer, and this price is low, Lyft can be almost sure that an Uber is close. Lyft can take advantage of this information and charge more given that Uber seems to be in dire need of a customer. Uber can make a similar argument why to pay less than their willingness to give, creating a plight of disagreement. Incomplete information does not allow some trades, even if they are efficient. (There is a famous and abstract [theorem](https://en.wikipedia.org/wiki/Myerson%E2%80%93Satterthwaite_theorem) along these lines.)

A system to facilitate the exchange of customers could make transportation in many urban areas more efficient. Building and integrating it into the marketplace is far from a trivial task, and will require some more summers before it will be finished. Before that, when starting to wrap up after an enjoyable day at the pond, remember to check all available ride-hailing apps.
