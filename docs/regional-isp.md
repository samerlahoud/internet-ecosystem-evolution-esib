# International ISPs in the Middle East

An ISP(Internet service providers) is a company that provides individuals and other companies access to the internet.An ISP has the equipment to provide internet to a specific geographic area. The larger ISPs have their own infrastructure so that they are less dependent on the telecommunication providers and can provide better service to their customers. However, there are 3 levels of ISPs. Tier 1, tier 2, and tier 3 providers.<br />
Tier 1 providers or backbone provider, exchange Internet traffic with other tier 1 providers via peering , or with other internet providers via transit.Without these providers there wouldn't be traffic exchange between continents.<br />
Tier 2 on the other hand are service providers which connect between tier 1 and tier 3 providers.<br />
Finaly Tier 3 ISP are providers that purchase internet transit and redistribute to their clients.<br />

In this project we are going to analyse the international ISPs for the MENOG region.All the measurements are being extracted from RIPE stat,for this study the data of the current time is being extracted by using the Request.get method witch is a simple HTTP request.
After the request the data is saved as json format. Json parsing will be the solution for using the information measured.<br />

Figure 1 shows a pie chart of the international transit providers of Lebanon in 2018. As we can see there are 3 major providers in lebanon:Level 3,Tata Communication,SEABONE-NET.These backbone providers will connect Lebanon to the world.We realise that more than 58% of lebanon is covered by Level 3 and one of the reasons of this dependency,could be the very attractive deal between the lebansses ISP and Level 3. However this pourcentage isn't as good as its looks like because there is no redundancy in the lebaneese network.

 ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB.png) <br />
Figure 1<br />
<br />
<br />
The table below shows the evolution of the International Providers of Lebanon from 2008 to 2018.<br />


| International Transit Providers in Lebanon | International Transit Providers in Lebanon |
| ------------- | ------------- |
| ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB_2008.png)  | ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB_2009.png) |
| ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB_2010.png)  | ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB_2011.png) |
| ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB_2013.png)  | ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB_2014.png) |
| ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB_2015.png)  | ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB_2016.png) |
| ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB_2017.png)  | ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB.png)  |

As we can see, the providers and their coverage changes every year. However some of them are still playing since 2008 a very important role in the connection of Lebanon with the world,like level 3.This backbone provider has been covering from 15 to 30% of Lebanon since 2010. <br />
On the other hand some of the International providers like BTT reduced their coverage in lebanon.While they covered more than 30% of lebanon in 2008, this pourcentage  dropped to 15%  in 2009.The attractive deals with other providers might explain this drop .After 2013 BTN, which was a very important provider for Lebanon, became part of the providers with less than 4% of coverage .However years go by and new International providers aren't connecting lebanon to their networks.<br />


| International Transit Providers in Lebanon | International Transit Providers in AE |
| ------------- | ------------- |
| ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/LB/LB.png)  | ![plot LB](https://raw.githubusercontent.com/samerlahoud/internet-ecosystem-evolution-esib/master/3-regional-isp/Graphs/AE/AE.png) |





