--
-- PostgreSQL database dump
--

-- Dumped from database version 14.15 (Homebrew)
-- Dumped by pg_dump version 16.9 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: accounts_customuser; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.accounts_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
34	pbkdf2_sha256$870000$iNMRrxW02lOxU8q7ez5h4y$mdStVnXusj6MdYeUXhhDu89ymL2E/0s8Q1KWlqqxB0U=	2025-05-07 20:22:42-04	f	josicki0704@gmail.com			josicki0704@gmail.com	f	t	2025-05-07 13:05:20-04
2	pbkdf2_sha256$870000$cMBrAwKnzzF9hx8nIjGMCx$xyqgP7VuERl8hBv9KIWVbtcnyNWxxXa/yEW6BB8JRNU=	2025-05-12 18:11:40.732315-04	f	ejartmover@gmail.com			ejartmover@gmail.com	f	t	2025-04-21 10:34:15-04
1	pbkdf2_sha256$870000$L72uq80jYkJurs66se1e0b$cVPODmApqy1YngEK69BNDqWh128+b4x8X2ZC55Pgv2Q=	2025-05-14 15:08:27.752392-04	t	mnraynor90@gmail.com			mnraynor90@gmail.com	t	t	2025-04-19 19:36:57.906174-04
100	pbkdf2_sha256$870000$2Q5T2URf0CupVLTif6idG4$LLeuY6qUwhTZ5CNInIGjGfEztf2uVzD5XUASMjF2twc=	2025-05-14 15:31:06.789243-04	f	bblueheron@gmail.com			bblueheron@gmail.com	f	t	2025-05-14 14:59:20-04
67	pbkdf2_sha256$870000$cZq3NbDPxqPWsAse3soKXL$M5diZQWiku4R+PyjUoIpA9v5METiD1hafOTqlAxfCH8=	2025-05-15 10:17:32.010216-04	f	stacy.a.gorman@gmail.com			stacy.a.gorman@gmail.com	f	t	2025-05-11 16:59:22-04
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
1	ejartmover@gmail.com
\.


--
-- Data for Name: accounts_customuser_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.accounts_customuser_groups (id, customuser_id, group_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	accounts	customuser
7	workorders	workorder
8	workorders	jobnote
9	workorders	jobattachment
10	workorders	event
11	clients	client
12	invoices	invoice
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_customuser
22	Can change user	6	change_customuser
23	Can delete user	6	delete_customuser
24	Can view user	6	view_customuser
25	Can add work order	7	add_workorder
26	Can change work order	7	change_workorder
27	Can delete work order	7	delete_workorder
28	Can view work order	7	view_workorder
29	Can add job note	8	add_jobnote
30	Can change job note	8	change_jobnote
31	Can delete job note	8	delete_jobnote
32	Can view job note	8	view_jobnote
33	Can add job attachment	9	add_jobattachment
34	Can change job attachment	9	change_jobattachment
35	Can delete job attachment	9	delete_jobattachment
36	Can view job attachment	9	view_jobattachment
37	Can add event	10	add_event
38	Can change event	10	change_event
39	Can delete event	10	delete_event
40	Can view event	10	view_event
41	Can add client	11	add_client
42	Can change client	11	change_client
43	Can delete client	11	delete_client
44	Can view client	11	view_client
45	Can add invoice	12	add_invoice
46	Can change invoice	12	change_invoice
47	Can delete invoice	12	delete_invoice
48	Can view invoice	12	view_invoice
\.


--
-- Data for Name: accounts_customuser_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.accounts_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
1	2	1
2	2	2
3	2	3
4	2	4
5	2	5
6	2	6
7	2	7
8	2	8
9	2	9
10	2	10
11	2	11
12	2	12
13	2	13
14	2	14
15	2	15
16	2	16
17	2	17
18	2	18
19	2	19
20	2	20
21	2	21
22	2	22
23	2	23
24	2	24
25	2	25
26	2	26
27	2	27
28	2	28
29	2	29
30	2	30
31	2	31
32	2	32
33	2	33
34	2	34
35	2	35
36	2	36
37	2	37
38	2	38
39	2	39
40	2	40
41	2	41
42	2	42
43	2	43
44	2	44
45	2	45
46	2	46
47	2	47
48	2	48
79	34	13
80	34	14
81	34	15
82	34	16
83	34	17
84	34	18
85	34	19
86	34	20
91	34	25
92	34	26
93	34	27
94	34	28
95	34	29
96	34	30
97	34	31
98	34	32
99	34	33
100	34	34
101	34	35
102	34	36
103	34	37
104	34	38
105	34	39
106	34	40
107	34	41
108	34	42
109	34	43
110	34	44
111	34	45
112	34	46
113	34	47
114	34	48
133	67	13
134	67	14
135	67	15
136	67	16
137	67	17
138	67	18
139	67	19
140	67	20
141	67	25
142	67	26
143	67	27
144	67	28
145	67	29
146	67	30
147	67	31
148	67	32
149	67	33
150	67	34
151	67	35
152	67	36
153	67	37
154	67	38
155	67	39
156	67	40
157	67	41
158	67	42
159	67	43
160	67	44
161	67	45
162	67	46
163	67	47
164	67	48
165	100	1
166	100	2
167	100	3
168	100	4
169	100	5
170	100	6
171	100	7
172	100	8
173	100	9
174	100	10
175	100	11
176	100	12
177	100	13
178	100	14
179	100	15
180	100	16
181	100	17
182	100	18
183	100	19
184	100	20
185	100	21
186	100	22
187	100	23
188	100	24
189	100	25
190	100	26
191	100	27
192	100	28
193	100	29
194	100	30
195	100	31
196	100	32
197	100	33
198	100	34
199	100	35
200	100	36
201	100	37
202	100	38
203	100	39
204	100	40
205	100	41
206	100	42
207	100	43
208	100	44
209	100	45
210	100	46
211	100	47
212	100	48
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	1	7
8	1	8
9	1	9
10	1	10
11	1	11
12	1	12
13	1	13
14	1	14
15	1	15
16	1	16
17	1	17
18	1	18
19	1	19
20	1	20
21	1	21
22	1	22
23	1	23
24	1	24
25	1	25
26	1	26
27	1	27
28	1	28
29	1	29
30	1	30
31	1	31
32	1	32
33	1	33
34	1	34
35	1	35
36	1	36
37	1	37
38	1	38
39	1	39
40	1	40
41	1	41
42	1	42
43	1	43
44	1	44
45	1	45
46	1	46
47	1	47
48	1	48
\.


--
-- Data for Name: clients_client; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.clients_client (id, name, email, phone, address) FROM stdin;
893	Pamela Morgan	pemcrosby@gmail.com	+1 212-431-4048	87 Crosby St, New York, NY 10012
926	Richard Fertig	fertigr@gmail.com	+1 (917) 334-7911	51 Dumar Drive Sag Harbor, NY
959	Annie Hamilton	Annie@lindroth.cc	\N	Lindroth Design
1025	Ellen Foldes	ellen@ellenfoldesartadvisory.com	+1 (914) 263-5038	\N
1058	Ben Segal	\N	+1 (917) 328-6494	122 Henry Road Southampton, NY
1091	Kasey Karp	\N	+1-917-923-6791	553 Wainscott NW Road, Wainscott, NY 11975
992	Steven Leibsohn	stevenmdstar@yahoo.com	+1 (623) 202-7114	303 Park avenue #1916
894	Mrs. Mathis	\N	+1 (516) 458-8001	8 Ogden Lane Quogue, NY
960	Don Christensen	\N	(347) 721-5856	\N
993	steven leibsohn	stevenmdstar@yahoo.com	+1 (623) 202-7114	303 Park avenue #1916 New York,NY
1059	Jeff Kraus	jk@carvalhopark.com	+1.231.590.5355	112 WATERBURY STREET, BROOKLYN, NY 11206
1092	Hillary Liebowitz	\N	+1-516-322-8390	885 Park Avenue, 5C, New York, NY
895	Jeff & Lynn Schwartz	\N	+1 (914) 450-6280	8 Great Oak Lane East Hampton, NY
961	Vidur Kapur	kapur.vidur@gmail.com	+1 (347) 581-5062	45 south midway road shelter island NY 11964
994	Annie Hamilton, Lindroth Design	Annie@lindroth.cc	\N	\N
1060	KATHRYN MARKEL FINE ARTS	\N	908.991.6940	529 W. 20th Street New York, NY
1093	Harron Zimmerman	\N	+1-917-297-4229	28 Second Neck Lane, Quogue, NY
962	Christine Wexler	cmwex5@gmail.com	+1 (914) 715-7257	\N
995	Patrick McGinley	\N	646-206-0887	\N
1061	Roderic Steinkamp	Roderic@rsteinkamp.com	+1 (917) 225-9019	47 The Circle East Hampton, NY 11937
1094	Jennifer Gross	jennifergross1@gmail.com	+1 (917) 693-6951	149 E. 73rd St., Apt. 10 A.
1062	Christine Wexler	cmwex5@gmail.com	+1 (914) 715-7257	\N
1095	Sheryl Kaye	sjk@thekayes.com	+1 (914) 450-8009	101 West 67th St, NY 10023
1063	Ellie	\N	+1 (917) 608-1010	\N
447	Patricia Calderoni		nan	1134 Harbor Dr Delray Beach Fl 33483
448	Samuel Waxman		nan	1158 Fifth Ave15B New York NY 10128
449	James Croak Tomoeito		nan	12 Northview Dr Sag Harbor NY 11963
450	Casey Kaplan		(646) 833-7709	121 West 27th Street New York NY 10001
451	Jane Hausman Troy		nan	170 Wainscott Harbor Road Sagaponack NY
452	Penny Kaplan		nan	2 5th Avenue#6M New York NY 10011
453	Eleanor Jinks		nan	229 Bergen St Brooklyn NY 11217
454	Stephen Harris		(631) 697-8000	27 E. 65th Street New York NY
455	Antonio Martins		nan	34 N 7th PH 1E Brooklyn NY 11249
456	Perry Burns		nan	390 Pantigo Rd East Hampton NY 11937
457	Linda Mintz		nan	4349 Noyac Rd. Sag Harbor NY
458	Padideh Raphael		nan	5 Bittersweet Lane Amagansett NY 11930 USA
459	Bsquared Projects		nan	514 Pantigo Rd East Hampton NY 11937
460	Gaby Massey		917 359 8205	53 Quaquanantuck Lane Quogue New York 11959 United States
461	Nina  Link		917-224-9388	6 Country Estates Road Westhampton, New York 11977. New York 11977 United States
462	South Etna Arts Foundations		nan	77 East 77th Street New York NY 10075
463	William Sherman		nan	80 Gould St East Hampton NY 11937
464	Amy Nagler		nan	850 Park AveAPT 6B New York NY 10075
465	Larry Fliegleman		nan	PO Box 238 Remsenburg NY 11960
466	Hamptons House Watching	1630FR@Hamptonshousewatching.com,office@Hamptonshousewatching.com	nan	163 Old Farm Rd Sagaponack NY 11963
467	Jill & Giorgio DeSantis	1jillcarlson@gmail.com	nan	
468	Jay Mandel	8ml@hamptonshousewatching.com	nan	
469	Tibor De Nagy Gallery (TDN)	aarnot@tibordenagy.com	nan	
470	BBANYC	abaranovich@bbanyc.com	nan	
471	Your Special Delivery Service (YSDS)	Accounting.nyc@ysds.com	nan	Your Special Delivery Service New York NY 10001
472	David Netto Design LLC	accounting@davidnettodesign.com,valyn@davidnettodesign.com	nan	
473	Skyframe	accounting@skyframe.com,suzan@skyframe.com	nan	
474	The Hampton Synagogue	accounting@thehamptonsynagogue.org	nan	
475	Adelita Flowers	adelita@juicepress.com	nan	
476	Frank Fort	adessaint@benvoliogroup.com	nan	
477	Adriane Flinn	adief@gmail.com	nan	
478	Winston Wächter Fine Art	alangyel@winstonwachter.com	212-255-2718	530 West 25th St. New York NY 10001
479	Bella Mancini Design	Alex@bellamancinidesign.com	nan	
480	Andrew and Tara Weinstock	alex@bellamancinidesign.com	nan	24 Dock Hollow Rd. Cold Spring Harbor
481	Alex Benrimon	Alex@Benrimon.com	nan	
482	Alex Freedman	alexandra.freedman@artsymail.com	nan	Artsy New York NY 10013
483	Alicia Murphy	alicia@aliciamurphydesign.com	nan	
484	Voltz Clarke	alistair@voltzclarke.com	nan	
485	Aliya and Aren LeeKong	aliya@aliyaleekong.com,acl@dbscp.com	nan	
486	Allison Garcy Interiors	allison@allisongarcyinteriors.com	(917) 584-7844	
487	Fritz Advisory	Allison@fritzadvisory.com	nan	
488	Amanda Wilkes	amanda@bhallamunro.com	nan	
489	Amanda Mulcahy	amulcahy@newbond.com	(347) 683-0067	
490	Andrea McCafferty	andreamc129@yahoo.com	nan	
491	Andre Bally	andrebally@gmail.com	nan	
492	Felrath Hines LLC	andrew@artfinancepartners.com	nan	41 E. 57th StreetSte 702 New York NY 10022
493	FOX-NAHEM	Andrew@foxnahem.com	nan	
494	Andrew Pilaro	andrew@pilaro.com	nan	
495	The House of Fine Art	andrew@thehouseoffineart.com	nan	
496	Emphasis Design	andrews@emphasisdesign.com	nan	
497	Andy Siegel	andysiegel345@gmail.com	nan	
498	Anna Zorina Gallery	anna@annazorinagallery.com	nan	
499	Berggruen Gallery	ap@berggruen.com,stephanie@berggruen.com	nan	10 Hawthorne Street San Francisco CA 94105
500	ARC Fine Art LLC	arcfineart@me.com	nan	
501	Hilton Contemporary	arica@hiltoncomtemporary.com	nan	716 N. Wells Chicago IL
502	Armann	armann@ao-atelier.com	nan	
503	White Room Gallery	art4thewhiteroomgallery@gmail.com	nan	The White Room Gallery Bridgehampton NY 11932
504	April Gornik	artnik@optonline.net,artnik@pipline.com	nan	61 Fresh Pond Rd Sag Harbor NY 11963
505	Ashley Masella	ashley@11-11-creative.com	nan	
506	Ashley Stark	ashleystarkkenner@gmail.com	nan	
507	Michelle Gerson Wattell	ashlyn@michellegerson.com	nan	160 Clubhouse Rd King of Prussia PA 19406
508	Mariska Hargitay	assistant@mariska.com	nan	
509	Audry Casusol	axcasusol@yahoo.com	nan	
510	Axiom Contemporary	axiomcontemporary@gmail.com	nan	
511	Baboo Imaging Graphics Inc	Baboo@baboodigital.com	nan	
512	Maiken Baird	bairdassistant@gmail.com	nan	38 Two Mile Hollow East Hampton NY
513	Barbara Macklowe	Barbaramacklowe@gmail.com	nan	
514	INGRAO, INC	bballard@ingraoinc.com	(212) 472-5400 (516) 502-8516	17 East 64th Street New York NY 11065
515	Samuel Owen Gallery	betsy@samuelowen.com	nan	
516	Betsy Mackey	betsymackey16@gmail.com	nan	836 Sagg Main Sagaponack NY 11962
517	Tanya Taylor	billmacd@mac.com	nan	
518	Harper's Books	bills@harpersbooks.com,bills@harpersgallery.com	nan	87 Newtown Lane East Hampton NY 11937
519	Blair Dibble	blair@blairdibble.com	nan	
520	Bryce Markus	bmarkus27@gmail.com	nan	42 Wainscott Stone Rd
521	Robert Fleischer and Katy Glass	bob.fleischer@mac.com	nan	
522	Bob Tabor Images	bobtaborimages@gmail.com	nan	
523	Bonnie Lautenberg	bonnie@bonnielautenberg.com,khim.davis@eassets.com	nan	
524	John Hummel	brad@johnhummel.com	nan	
525	Brandigall	Brandigall@yahoo.com,Alisa.doctoroff@gmail.com	nan	
526	Kim Braswell	braswell.kimberly@gmail.com	nan	
527	Brian Leighton Inc	brian@brianleightoninc.com	(917) 403-5850	
528	Miles McEnery Gallery	brigid@milesmcenery.com	nan	
529	Victoria	britvic@me.com	nan	Third Way Construction
530	Bonnie Rychlak	brychlak09@gmail.com	nan	35 Neck Path East Hampton NY 11937
531	Beth Scharfman	bscharfman@gmail.com	nan	
532	Budd Goldman	bsg@finalwordinvestments.com	nan	
533	Goei	carey@goeidepiante.com, victoria@goeidepiante.com	nan	
534	Bjorn Design	carol@bjornendesign.com	nan	
535	Sandy Robertson	carol@carolsaper.com	nan	
536	Carrol Rominoff	carol@romanoffelements.com	nan	
537	Carola Beeney	carola.beeney@gmail.com	nan	
538	Carol Hunt	carolhunt125@icloud.com	nan	
539	Dekar Design	Caroline@dekardesign.com	nan	
540	FLAG Art Foundation	caroline@FLAGartfoundation.org	nan	
541	Frampton Co	casey@framptonco.com	nan	
542	Cassi Namoda	cassi.namoda@gmail.com,briannaashe@gmail.com,mchoi@agsny.com	nan	
543	ATP.art	cassie@atp.art.com	nan	511 6th Ave#934 New York NY 10011
544	MM Fine Art	catherine@mmfineart.com	nan	
545	Cathy Glass Design	cathy@cathyglassdesign.com	nan	
546	Berry Campbell, LLC	cb@berrycampbell.com	nan	530 W 24th St. New York NY 10011
547	Century Association	ccuadrado@thecentury.org	nan	7 W. 43rd St. New York NY 10036
548	Clic Gallery	centre@clic.com,accountspayable@clic.com	nan	255 Centre Street New York NY 10013
549	Chandler Smith	Chandlers@gmail.com	nan	
550	Charlie Ferrer	charlie@ferrer.co,isadora@ferrer.co	nan	
551	Chase Edwards Contemporary	chaseedwardsgallery@gmail.com	nan	2462 Main Street Bridgehampton NY 11932
552	Karen Kelly	Chefmarina2020@gmail.com	nan	
553	Cheryl Hazan	cheryl@cherylhazan.com	nan	35 N Moore St. #1 New York NY 10013
554	Atelier Purcell	cherylg@atelierpurcell.com,alex@alexandrepurcellrodrigues.com	nan	
555	Audrey Flack	chloepitkoff@gmail.com,severin.delfs@gmail.com,audreyflack@hotmail.com	nan	
556	Chris Hansen	chrishansen.la@mac.com	nan	
557	AWG Art Advisory	christine@awgartadvisory.com	nan	Christine
558	Scott Rudin	claudia@benjaminvandiver.com	nan	
559	Marjonne	Contact@twishippers.com	nan	
560	Cornelia Foss	corneliafoss@aol.com	nan	
561	DAD Trucking Inc.	dadny@verizon.net	nan	855 Edgewater Road Bronx NY 10474
562	Damien	damien@abeartllc.com	nan	
563	Damien Roman Fine Art	damien@damienromanfineart.com,damien@romanfineart.com	nan	
564	Dan Glaser	Dan.glaser@mmc.com,Felicia.Fink@mmc.com	nan	
565	Dana Rubin	Danarubin@optonline.net	nan	
566	Aetna Fine Art Logistics	daniel.l@aetnafineart.com,Stephen.B@AetnaFineArt.com,Rick.P@AetnaFineart.com	1-516-825-5885  Ext. 103	123 E Mineola Ave Valley Stream NY 11580
567	Matthew Marks Gallery	daniela@matthewmarks.com	nan	
568	Dan Nguyen	dannguyen39@Yahoo.com	(908) 698-3383	
569	David Molner	david.molner@gmail.com	nan	
570	David and Sarah Schimmel	david@andpartnersny.com	nan	108 E 86th St. New York NY 10028
571	Dawn	dawn@serhant.com	nan	
572	Daniela Carrasco	dearteclub@gmail.com	nan	
573	Debbie Perlick	debbieperlick@aol.com	nan	
574	Buck House LLC	deborah@deborahbuck.com,deborah@deborahbuck.com	nan	
575	Denise Incandela	deniseincandela@gmail.com	nan	1000 Park Avenue#4B New York NY 10028
576	Jasmine Lam	design@jasminelam.com	nan	927 Lincoln RoadSuite 200 Miami Beach FL 33139
577	Dennis Ferrone	dfhomeinc@gmail.com	nan	
578	Douglas Maxwell	dfmaxwell@mac.com	nan	
579	Dana Golding	dgolding@abromgmt.com	nan	
580	Steve Diamond	diamondsteve7@gmail.com	nan	25 W. 81st St. New York NY 10024
581	Margherita Divari	divari@massimodecarlo.com	nan	16 Clifford Street  W1S 3RG London   United Kingdom
582	David Israel	dji6262@aol.com	nan	142 Old Northwest Road East Hampton NY 11937
583	Affiliated Adjustment Group Ltd.	dklein@adjustmentgroup.com	nan	3000 Marcus Ave\nSte 3W3 Lake Success NY 11042
584	Daryl Goldberg-Simon	dns4hk@gmail.com	nan	
585	Dorian Bergen	dorian@acagalleries.com	nan	
586	Dream Windows & Interiors, LLC	dreamwindows11977@gmail.com	nan	29 Montauk Highway Westhampton NY 11977
587	Drew Shiflett	dshiflett@yahoo.com	nan	
588	Southampton Art Center	dtorres@southamptoncenter.org,tcmotch@southhamptoncenter.org,jdiamond@southamptoncenter.org	nan	
589	Duck Creek Arts	duckcreekarts@gmail.com	nan	
590	Gregory McKenzie	duhallowgregm120@aol.com	nan	14 Mill Farm Southampton NY 11968
591	Darius Yektai	dyektai@gmail.com	nan	
592	Dyektai	Dyektai@gmail.com	nan	
593	Denny Dimin Gallery	dylan@dennydimingallery.com	nan	
594	Elizabeth Bolognino Interiors LLC	EB@elizabethbolognino.com	nan	
595	Another Space	ebbrodsky@gmail.com, harqueta@anotherspace.org	nan	
596	Elliot Cooperstone	ecooperstone@gmail.com	nan	
597	Eleanor Donnelly	ed@stelleco.com,jb@stelleco.com	nan	
598	Elissa DeBrito	edebrito1@aol.com	nan	29 East Hollow Road East Hampton NY 11937
599	Emma DeGennaro	edegannaro@ingraoinc.com	nan	
600	Judy Gibbons	edenfelicien@gmail.com	nan	8500 Flourtown Ave Wyndmoor PA
601	Tulla Booth Gallery, LLC	edwardsegal0@me.com, edward.segal@gmail.com	nan	66 Main St Sag Harbor NY
602	Elizabeth Hazan	ehazan@mindspring.com	nan	20 Jay Street Brooklyn NY 11201
603	Eileen Ekstract	eileenekstract@gmail.com,eileen.ekstract@collectorsconcessions.com	nan	
604	Russell Steel	ejartmover@gmail.com	nan	
605	Michael John Silverton	Ejartmover@gmail.com	(312) 576-5922	80 Further Lane East Hampton NY 11937
606	Elephant Designs	elephantdesigns@me.com	nan	
607	Michael Del Piero Good Design	elizabeth@michaeldelpiero.com	nan	
608	Ellen	Ellen@ellenfoldesartadvisory.com	nan	
609	John Alschuler	Emily.Foster@therme.us	nan	
610	Emily	emily@emilydbinteriors.com	nan	
611	Eric Wuu	eric@allisongarcyinteriors.com	nan	
612	Effie Tstitiridis	etsitiridis@gmail.com	nan	
613	Frank Born	fborn12@gmail.com	nan	
614	Eric Fischl	fischlstudio@gmail.com	nan	
615	Open House LTD	frank@foronjy.com	nan	
616	Findlay Galleries	fred@findlayart.com	(212) 421-5390	165 Worth Avenue Palm Beach FL 33489
617	George Billis Gallery	gallery@georgebillis.com,georgebillisgallery@yahoo.com	nan	
618	Gavin Spanierman	gavin@gspanierman.com	nan	
619	Gene Bernstein	geneb@northville.com	nan	
620	Parthenon	george@parthenonframing.com	nan	
621	Katherine Gleason	gleason.kathryn@gmail.com	nan	
622	Kathryn Gleason	gleason.kathryn@gmail.com	nan	
623	Gayle Lopata	glopata@bhsusa.com	nan	
624	Gary Moross	gmoross@gmail.com	nan	
625	Gianna Putrino	gputrino@nyaa.edu	nan	
626	Rebecca Grafstein	grafsteinr@gmail.com	nan	
627	Greg Carter Studio Management	gregcarter.theone@gmail.com	nan	
628	Gregory Kong	gregorykong@gmail.com	nan	
629	Galerie Kornfeld	hakobyan@galeriekornfeld.com	nan	Galerie KornfeldKunsthandel GmbH & Co.KGFasanenstr. 26 Berlin  10719 Germany
630	Mr. Arslanian	hanisha@aarslanian.com	(917) 892-8864	
631	Venus Over Manhattan	Heather@venusovermanhattan.com	nan	
632	Adhesivo LLC	Hello@adhesivomagazine.com	nan	20379 W. Country Club Dr.#2439 Aventura Fl 33180
633	Destination Haus	hello@destinationhaus.com	nan	55 Main Street East Hampton NY 11937
634	Hilary Matt	hilary@hilarymatt.com	nan	
635	Helen Gifford	hlgifford1@yahoo.com	nan	P.O Box 61 Sag Harbor NY 11963
636	Holly Levy	hollylevy@aol.com	nan	10 East Wood Path Sagaponack NY
637	Hope Rothschild	hoperothschild@yahoo.com	nan	
638	Keewaydin Investments	hrr@keewaydininvestments.com	nan	
639	Heather Sherman	hsherman543@gmail.com	nan	
640	Claire Oliver Gallery	ian@claireoliver.com	nan	
641	Ilene Sands	ibeth103@aol.com	nan	
642	Abe Art LLC	info@abeartllc.com	nan	
643	Cavin Morris Gallery	info@cavinmorris.com	nan	
644	Plant house	info@planthouse.net	nan	
645	Rental Gallery	info@rentalgallery.us	(631) 903-7474	
646	Cristin Longo	info@spondergallery.com	nan	
647	Sponder Gallery	info@spondergallery.com	nan	
648	Intense Movers	intensemovers@gmail.com,aleute3@gmail.com	nan	
649	Irina Alimanestianu	irina@irinaalimanestianu.com	nan	
650	Irving Grauer	irving.grauer@gmail.com	nan	5 Farrell Ct Watermill NY 11976
651	Isaac Reynoso	isaac@culturalproducations.com,melissa@culturalproductions.com	nan	
652	Inplus Inc.	isao@inplusinc.com	nan	
653	Jessica VonHagn	j.vonhagn@compass.com	nan	
654	Jackie Paolone	jacquelinepaolone@mac.com	nan	
655	James DeMartis Metal Studio	james@jamesdemartis.com	nan	
656	McAlpine House	janderson@mcalpinehouse.com	nan	
657	Janet Jennings	janetjenningsart@gmail.com	nan	
658	Janet Lehr	janetlehr@janetlehrinc.com	nan	
659	Joseph Bell	jbell@lbbelon.com	(917) 750-3460	95 Davids Lane East Hampton NY
660	Jay Bialsky	jbialsky@icloud.com,jay@jbialsky.com	nan	
661	Natalie	Jcohenhousehold@gmail.com	nan	28 West End Road East Hampton
662	J Design Group	jdesigngroup@aol.com	nan	
663	Jean Albano Gallery	jeanalbanogallery@gmail.com	nan	
664	Jeff Lincoln	jeff@collectiveartdesign.com	nan	
665	Jen Going Interiors JDG	jen@jengoinginteriors.com,betty@jengoinginteriors.com	nan	
666	Jessica Cohen Designs	jessica@jessicacohendesigns.com	nan	
667	Jessica Lichtenstein	jessica@jessicalichtenstein.com	nan	710 Broadway New York NY 10003
668	Jonathan Grayer	jg@jgrayer.com	nan	
669	Jennifer Whitman	jgwhitman2000@yahoo.com	nan	113 Farm Field Road Bridgehampton NY 11932
670	Jim Daiyle	jimdny@gmail.com	nan	
671	The American Academy of Arts & Letters	Jjaskey@artsandletters.org	nan	
672	Carvalho Park Gallery	jk@carvalhopark.com	nan	
673	Cromwell Art	jkopie@mac.com, jeff@cromwellart.com	nan	119 W. 72nd St#131 New York NY 10023
674	Jeff Muhs	jmuhs@jeffmuhsstudio.com	nan	
675	High Fashion Concepts	joanna@hfcart.com	nan	
676	Joanna	joanna@venusovermanhattan.com	nan	
677	Joanne Carson Art Studio	joannecarsonartstudio@gmail.com,suzanne@suzanneunrein.com	nan	
678	Joanne Greenbaum	joannegreenbaum@me.com	917-476-8652	519 Sterling place Greenport ny 11944
679	Paula Cooper Gallery	joe@paulacoopergallery.com	(212) 255-1105	524 West 26th Street New York NY 10001
680	Joel Mesler	joel@rentalgallery.us	nan	
681	John Picker	john@johnpicker.com	nan	
682	John Alexander	johnalexanderstudio@gmail.com	nan	
683	John Acierno	johnlacierno@gmail.com	nan	
684	Jonathan Boos	jonathanboos@mac.com,minnie@jonathanboos.com,sheri@jonathanboos.com	nan	
685	Kathy Kuo Home	jordan@kathykuohome.com	nan	Kathy Kuo Home30 Jobs Lane Southampton NY 11968
686	Josef Najar	josef.najar@morganstanley.com	(917) 690-2900	52 Ruxton Road East Hampton NY 11937
687	Jennifer Gardner	jrgardner47@gmail.com	nan	
688	C and C Gallery	julia@candcgallery.com	nan	
689	Rebecca Hossack Gallery	julia@rebeccahossack.com	nan	
690	One Main (The BZZAAR Inc.)	julianna@one1main.com	nan	Artsyc/o Alex Freedman401 Broadway, Floor 25 New York NY 10013
691	Keyes Art Gallery	juliekeyes15@yahoo.com	nan	
692	Kai Gallery LLC	justin@kaigallery.com	nan	
693	Agora Gallery	justinrosswarner@gmail.com	nan	530 W. 25th St New York NY
694	Jutta Kraus	jutta@ruttkowski68.com	nan	8 Rue Charlot, 75003Paris, France
695	Juvy Miraflor	juvy63sm@yahoo.com	nan	
696	Joan Holden	jzholden67@gmail.com	nan	
697	Joe Farrell	k.kelly@farrellbuilding.com	nan	
698	Catalyst Art	Kahl@catalystartinc.com	nan	
699	Susana Simonpietri	kaitlin.kelly@chango.co	nan	Susana Simonpietri East Hampton NY 11937
700	Eric Firestone Gallery	Kara@ericfirestonegallery.com	nan	
701	Contessa Gallery	karen@contessagallery.com	nan	
702	Elements In Play	karen@elementsinplay.com	nan	
703	Hesse Flatow LLC	karen@hesseflatow.com	nan	127 Squaw Road East Hampton New York 11937 United States
704	Bonhams New York	Kate.Stamm@bonhams.com	nan	580 Madison Avenue New York NY 10022
705	Long House Reserve	kate@longhouse.org	nan	
706	Hauser & Wirth	katherinewilson@hauserwirth.com	nan	542 W. 22nd Street New York NY 10011
707	Katie Lydon Interiors	Kathryn@katielydoninteriors.com	nan	
708	KMR Arts	kathy@kmrarts.com	nan	
709	Kathy Markel	kathy@markelfinearts.com	nan	
710	Karen Bromberg	kbromberg@cohengresser.com	nan	
711	Cultural Counsel	keeley@culturalcounsel.com	nan	
712	Kelli Hull	kelli@kellihull.com	nan	
713	Kelly & Henry Prince	Kelly@prince.co,henry@prince.co	nan	
714	Katie Leede	kelsey@katieleede.com	nan	
715	Dominick Rotondi	ken@drdnyc.com	nan	
716	Kevin Hart	kevin@kevinhart.com	nan	
717	Khim Davis	khim.davis@eassets.com	nan	
718	James Cohan Gallery	klay@jamescohan.com	nan	
719	Parrish Art Museum	klopferr@parrishart.org	nan	
720	Mike Schneider	koufax77292@gmail.com	nan	
721	Montauk Yacht Club	kprugginteriors@gmail.com	nan	
722	Kramoris Gallery	kramorisgallery@gmail.com	nan	
723	Francoise Ghebaly	kristina@ghebaly.com	nan	
724	Kimberly Yoon	kyoon145@gmail.com	nan	
725	Larry Kane	larrykane123@gmail.com	nan	
726	Laura Solomon	laura@laurasolomonfineart.com	nan	
727	Joline Stemerman	laurence@stmrhome.com	nan	
728	Laurence	Laurence@stmrhome.com	nan	
729	Linda Burkhardt	LB@lindaburkhardt.com	nan	
730	Lisa Guida	Lbguida@me.com	nan	
731	Leslie Ghize	lghize@tobereport.com	nan	
732	The Noguchi Museum	lgiacoletti@noguchi.org	nan	
733	Lilly Bunn	Lilly@lillybunn.com	nan	
734	Linda J Sirow	linda.sirow@gmail.com	nan	
735	Nino Mier Gallery	lindsey@miergallery.com	nan	
736	Kemble Interiors	liza@kembleinteriors.com	nan	
737	Liz Vayner	lizvayner@gmail.com	nan	
738	Lisa Marie Milat	lm@studioelleemme.com	nan	
739	Lochen Design	lo.chen@lochendesign.com	nan	
740	Louise P. Sloane	Lps11@optonline.net	nan	50 Kings Point Road Kings Point NY 11024
741	Lani Shufelt	lshufelt@thechanler.com	nan	
742	Laura Traphagen	ltraphagen@gmail.com	nan	
743	Lynn Savarese	lynn.savarese@gmail.com	nan	
744	Lynn Avenue, LLC.	LynnAvenueLLC@CaiolaREgroup.com	nan	99 Lynn Ave. Hampton Bays NY 11946
745	Laurie Zucker	LZucker@mskyline.com	631-537-7797	101 West 55th Street New York NY 10019
746	Maggie Tolkin	maggie.tolkin@gmail.com	nan	
747	Michael Altman	maltman@mnafineart.com	nan	
748	Pure Art Services	margaret@pureartservices.com	nan	
749	The Selects Gallery	marie@theselectsgallery.com	nan	
750	Embed Creative	Marisa@embedcreative.com	nan	
751	Katja Goldman	marisol.marquez@muus.com	nan	
752	Mayrock Art	Marjorie@mayrockart.com	nan	
753	Serena & Lily	mark.hughes@serenaandlily.com	nan	
754	Building Details	mary@buildingdetails.com	nan	103 Montauk Hwy East Hampton NY
755	Nicole Klagsbrun Inc	mary@nicoleklagsbrun.com	nan	
756	Vallarino Fine Art	masha@vallarinofineart.com	(212) 628-0722	
757	Matt Shamnoski	matt.sham77@gmail.com	nan	
758	Dietl	matthew.hickey@dietl.com	nan	207 W. 25th St.FL 3 New York NY
759	Michael Aviles	maviles@mjavileslaw.com	nan	
760	Darrow Contemporary	maxine@darrowcontemporary.com	nan	
761	Sean McCarthy	mccarthy.sean.w@gmail.com	nan	
762	Leyden Lewis	mczappacosta@gmail.com	nan	
763	Miles Jaffee	mdj@milesjaffe.com	nan	
764	Max Dolgicer	mdolgicer@isg-inc.com	nan	
765	Grenning Gallery	megan@grenninggallery.com	631-725-8469	Laura Grenning Sag Harbor NY 11963
766	Megan Riley	megan@meganriley.com	nan	
767	Brian J. McCarthy	melanie@bjminc.com	917-304-9118	Brian J. McCarthy57 West 57th Street New York NY 10019
768	Markt Art Advisory	Meredith@marktadvisory.com	nan	
769	Meredith Keay	meredithkeay@me.com	nan	
770	MFS Sculpture Jewelry	mia@miafsolow.com	nan	
771	Michal Mufson	michal@michalmufson.com	nan	
772	Nicole Brady	michellepeirona@gmail.com	nan	50 Highway Behind the Pond East Hampton NY 11937
773	Sag Harbor Cinema	mimi@sagharborcinema.org,iwona@sagharborcinema.org	nan	
774	Mindy & Daniel Bass	mindybass409@gmail.com	nan	350 Mecox Road Water Mill NY
775	Miriam	miriam@mwldesigngroup.com	nan	
776	Marie Josée Primeau	mjp@mariejoseeprimeau.com	nan	
777	Mickey Baumrind	mmbaumrind@gmail.com	nan	
778	Marty Melzer	Mmcpapc@aol.com	(631) 766-5222	PO Box 905 Remsenburg NY 11960
779	New York Academy of Art	msmith@nyaa.edu,helbers@nyaa.edu	nan	
780	Meryl Taradash	mtarnyc@aol.com	nan	
781	Mike Chutko	mtchutko@gmail.com	nan	
782	Mary Weatherford Inc.	mw@maryweatherford.net	nan	
783	Nadia Anderson	nadia.hackett@gmail.com	nan	
784	Mark Lehr	Nancy@laanda.net	nan	
785	Nancy Larsen	nancy@laanda.net	nan	
786	Marc Leder	nancy@laanda.net	nan	Sagg Main Holdings, LLCAttn:  Family Office5200 Town Center Circle, 4th Floor Boca Raton FL 33486
787	Casterline Goodman Gallery	natalie@casterlinegoodman.com	nan	
788	Natalie Antoine	natalie@casterlinegoodman.com	nan	
789	Nick Dietz	nick@thelifestylerguy.com	nan	
790	Hidden Lake Asset Management	Nicole@hiddenlakeam.com	(212) 237-1280 (347) 668-1693	52 West 57th Street, Suite 920 New York NY 10019
791	Paul. Davis	nik.jajac@pauldavis.com	nan	
792	Nikki Brown	Nikki@nikkilbrownart.com	nan	
793	Samuels Creative & Co.	nina@samuelscreative.com,es@samuelscreative.com	nan	
794	Norman Weisfeld	normanw@fubu.com	nan	12 Windsor Gate Great Neck NY 11021
795	Nathan Strieter	nstrieter@lsm.com	nan	
796	Corder Management	office@cordermanagement.com	nan	
797	Dan Hasted	office@manage-ment.com	nan	
798	Oscar Junquera	ojunquera@panmarcap.com	nan	
799	Omar Baker	omar.md@gmail.com	nan	
800	Phillip Danisi	p.danisi7@gmail.com	nan	
801	Patricia McGrath Design	patricia@pmcgrathdesign.com	631-537-2822	Decorative Detail Interiors
802	Michael Davis	Patrick@michaeldavis.com	nan	
803	Patrick Creedon	patrickc@taymourgrahne.com	nan	
804	Clifford Ross	paul@cliffordross.com	nan	
805	Paul Davis	paul@pauldavisnewyork.com	nan	
806	Peter Buchman	pbucks@optonline.net	nan	
807	Guild Hall East Hampton	pcontent@guildhall.org	nan	
808	Perry Steiner	perrywintersteiner@gmail.com	nan	
809	Peter Dayton LLC	peter@peterdayton.com	nan	
810	Peter Simon	peter@pmsimon.ch	nan	
811	Peter Genatt	pgenatt@aol.com,tgenatt@gmail.com	nan	34 Leonard St. PH NY NY 10013
812	Blond Contemporary	philli@blondcontemporary.com	nan	
813	Mark Borghi Fine Art Inc.	phoebe@markborghi.com,mark@markborghi.com,mark@borghi.org	nan	2426 Main St. Bridgehampton NY 11930
814	Peter Lee	plee70376@gmail.com	nan	
815	Benrubi Gallery	rachel@benrubigallery.com	nan	
816	Tina Kim Gallery	rachel@tinakimgallery.com	646-939-5098	525 West 21st Street New York NY 10011
817	Robert Guida	raguida@me.com	914-222-5000	
818	Randi Ball	randi.ball@corcoran.com	nan	
819	Rebecca Homapour	rebeccadcohen@gmail.com	nan	
820	Robin Matza Design	redhead1160@aol.com,robin.matza@serenaandlily.com	nan	
821	Peggy Gelfond	reply2peggy@gmail.com	nan	
822	Richard Rothschild	richard.rothschild56@gmail.com	nan	
823	Richard Friedman	rick@show-hamptons.com	(631) 283-5505	
824	Dan Rizzie	rizvex@optonline.net	nan	
825	Front Desk Apparatus	rob@frontdeskapparatus.com	nan	
826	Pie Pie MTK LLC	rosa@meteorvineyard.com	nan	20 Hamilton Drive Montauk NY 11954
827	University of Lynchburg	rothermel@lynchburg.edu	nan	
828	Colm Rowan Fine Art	rowan.colm@gmail.com	nan	55 Main Street East Hampton NY 11937
829	By Appointment Hamptons	ryan@byappointmentshamptons.com	nan	
830	I.V. Contemporary LLC	sandrac@institutodevision.com	nan	88 Eldridge St NY NY
831	Brooke Abrams Design	sara@brookeabramsdesign.com	nan	
832	Nightingale Gallery	sara@saranightingale.com	nan	
833	Sears-Peyton Gallery	sarah@searspeyton.com	nan	
834	The Journal Gallery	sarah@thejournalgallery.com	nan	45 White Street New York NY 10013
835	Susanna Adler	sarahjbarkow@gmail.com	nan	
836	Michael Schubert	schubert@ruderfinn.com	nan	
837	Roy Seifert	seifertroy@gmail.com	nan	
838	Sara Fitzmaurice	sfitzmaurice@aventure-art.com	nan	
839	Mitchell-Innes & Nash, Inc.	Sheldon@miandn.com	2127447400	526 W 26th St Rm 308 New York NY 100015518 US
840	Sheri Sandler	sheri@sherisandler.com	nan	
841	Michael Weinberg	sheri@thechurchsagharbor.org	nan	
842	The Church Sag Harbor	sheri@thechurchsagharbor.org	nan	
843	Susan Kane	skane275@hotmail.com	nan	105 Cove Hollow East Hampton NY 11937
844	Shawn Levy	slevy@mlmgmt.com,salevy@mac.com	nan	
845	Swann Auction Galleries	slicitra@swanngalleries.com	nan	
846	Sloan Schaffer	sloan@101exhibit.com	nan	210 Cold Spring Rd Hudson NY 12534
847	David Scott	sloane@davidscottinteriors.com	nan	
848	Sloane Hubbuch	sloane@davidscottinteriors.com	502-744-6527	50 Lawrence Ct Water Mill NY 11976 United States
849	Sylvia Oberwager	sloberwager@gmail.com	nan	68 Mecox Road Watermill NY 11976
850	Steve Cohn	smcohn911@gmail.com	nan	
851	Hollis Taggart	smgolden@hollistaggart.com,stancharnin@hollistaggart.com	nan	
852	Eli Wilner & Co. INC	smorello@eliwilner.com	nan	
853	MARIANNE BOESKY GALLERY	sophia@boeskygallery.com	nan	
854	Stafford Broumand	srbroumand@gmail.com	nan	
855	Stefani Shavel	stefani.shavel@gmail.com	nan	
856	Julie Stelzer	stelzerjulie@gmail.com	nan	
857	Allan Schwartzman	stephen@allanschwartzman.com	nan	
858	Steve Rabin	stever926@gmail.com	nan	
859	Stewart Gross	stewart@stewartgross.com	Office 212-328-0548  917-903-7260	Lightyear Capital New York NY 10019
860	Stuart Rothstein	stuartrothstein@yahoo.com	nan	
861	DFI Services / Adco Group	sue.ball@adcogroup.com	nan	
862	Sue Ball	sue.ball@adcogroup.com	nan	
863	N 53 Gallery	summer@n53gallery.com, weiss@n53gallery.com	(718) 755-9052	53 the Circle East Hampton
864	Caldwell Snyder	susan@caldwellsnyder.com,liz@caldwellsnyder.com	nan	
865	Susan Gross	susan@grossarch.com	nan	
866	North Shore Cosmetic	susanpacifico@hotmail.com	nan	
867	Suzanne Anker	suzanne.anker@gmail.com	nan	
868	Lori Margolis Interiors	sydney@lorimargolisinteriors.com,lori@lorimargolisinteriors.com	nan	
869	S Bitter-Larkin Fine Art Inc.	sylviebitterlarkin@gmail.com	nan	PO Box1957 Shelter Island NY 11964
870	Stephen Zaro	sz@lancewoodcapital.com	nan	
871	Christine Blaustein	T90winter@hotmail.com	nan	
872	Suffolk Community College Association Inc.	teasond@sunysuffolk.edu,gosnelm@sunysuffolk.edu	nan	
873	Terri Hyland	terrimhyland@gmail.com	nan	
874	Theodore Rojos	theodore.rojas@eassets.com	nan	
875	Espinasse31 INC	thomas@espinasse31.com	nan	929 Michigan Ave Miami Beach FL 33139
876	Mary Ryan Gallery	Thomas@maryryangallery.com	nan	
877	Ryan Lee Gallery	thomas@ryanleegallery.com	nan	
878	Thomas Gleeson	thomasgleeson@icloud.com	nan	215 Chrystie Street #28W New York NY 10002
879	Yarger Fine Art	tim@yargerfineart.com	nan	
880	Tim O'Conner	timothyollc@gmail.com	nan	
881	Bay Street	tracy@baystreet.org	nan	
882	Buckner Projects	troybuckner@mac.com	nan	
883	David Nolan Gallery	Valentina@davidnolangallery.com	nan	
884	Mckenzie Fine Art	valerie@mckenziefineart.com	nan	
885	Vered Art	Vered@veredart.com	nan	
886	Victoria Katsov	vkatsov@gmail.com	nan	
887	Turnberry	vpinera@turnberry.com	nan	
888	Ocean Graphics	Will@oghamptons.com	nan	
889	Juanita Wimberley	wimberleyf@nyc.rr.com	nan	
890	Morrison Gallery	wm.@morrisongallery.com,ellie@morrisongallery.com	nan	
891	Wendy Frieder	wmfrieder@gmail.com	nan	
892	Yanina Fuertes	ymfuertes@gmail.com	nan	
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2025-04-21 10:13:21.480556-04	447	Patricia Calderoni	1	new through import_export	11	1
2	2025-04-21 10:13:21.480604-04	448	Samuel Waxman	1	new through import_export	11	1
3	2025-04-21 10:13:21.480622-04	449	James Croak Tomoeito	1	new through import_export	11	1
4	2025-04-21 10:13:21.480638-04	450	Casey Kaplan	1	new through import_export	11	1
5	2025-04-21 10:13:21.480653-04	451	Jane Hausman Troy	1	new through import_export	11	1
6	2025-04-21 10:13:21.480668-04	452	Penny Kaplan	1	new through import_export	11	1
7	2025-04-21 10:13:21.480683-04	453	Eleanor Jinks	1	new through import_export	11	1
8	2025-04-21 10:13:21.480697-04	454	Stephen Harris	1	new through import_export	11	1
9	2025-04-21 10:13:21.480711-04	455	Antonio Martins	1	new through import_export	11	1
10	2025-04-21 10:13:21.480726-04	456	Perry Burns	1	new through import_export	11	1
11	2025-04-21 10:13:21.48074-04	457	Linda Mintz	1	new through import_export	11	1
12	2025-04-21 10:13:21.480754-04	458	Padideh Raphael	1	new through import_export	11	1
13	2025-04-21 10:13:21.480768-04	459	Bsquared Projects	1	new through import_export	11	1
14	2025-04-21 10:13:21.480782-04	460	Gaby Massey	1	new through import_export	11	1
15	2025-04-21 10:13:21.480796-04	461	Nina  Link	1	new through import_export	11	1
16	2025-04-21 10:13:21.480811-04	462	South Etna Arts Foundations	1	new through import_export	11	1
17	2025-04-21 10:13:21.480825-04	463	William Sherman	1	new through import_export	11	1
18	2025-04-21 10:13:21.480839-04	464	Amy Nagler	1	new through import_export	11	1
19	2025-04-21 10:13:21.480853-04	465	Larry Fliegleman	1	new through import_export	11	1
20	2025-04-21 10:13:21.480867-04	466	Hamptons House Watching	1	new through import_export	11	1
21	2025-04-21 10:13:21.480881-04	467	Jill & Giorgio DeSantis	1	new through import_export	11	1
22	2025-04-21 10:13:21.480896-04	468	Jay Mandel	1	new through import_export	11	1
23	2025-04-21 10:13:21.48091-04	469	Tibor De Nagy Gallery (TDN)	1	new through import_export	11	1
24	2025-04-21 10:13:21.480924-04	470	BBANYC	1	new through import_export	11	1
25	2025-04-21 10:13:21.480938-04	471	Your Special Delivery Service (YSDS)	1	new through import_export	11	1
26	2025-04-21 10:13:21.480958-04	472	David Netto Design LLC	1	new through import_export	11	1
27	2025-04-21 10:13:21.480975-04	473	Skyframe	1	new through import_export	11	1
28	2025-04-21 10:13:21.480989-04	474	The Hampton Synagogue	1	new through import_export	11	1
29	2025-04-21 10:13:21.481004-04	475	Adelita Flowers	1	new through import_export	11	1
30	2025-04-21 10:13:21.481018-04	476	Frank Fort	1	new through import_export	11	1
31	2025-04-21 10:13:21.481032-04	477	Adriane Flinn	1	new through import_export	11	1
32	2025-04-21 10:13:21.481047-04	478	Winston Wächter Fine Art	1	new through import_export	11	1
33	2025-04-21 10:13:21.481061-04	479	Bella Mancini Design	1	new through import_export	11	1
34	2025-04-21 10:13:21.481076-04	480	Andrew and Tara Weinstock	1	new through import_export	11	1
35	2025-04-21 10:13:21.48109-04	481	Alex Benrimon	1	new through import_export	11	1
36	2025-04-21 10:13:21.481104-04	482	Alex Freedman	1	new through import_export	11	1
37	2025-04-21 10:13:21.481118-04	483	Alicia Murphy	1	new through import_export	11	1
38	2025-04-21 10:13:21.481133-04	484	Voltz Clarke	1	new through import_export	11	1
39	2025-04-21 10:13:21.481147-04	485	Aliya and Aren LeeKong	1	new through import_export	11	1
40	2025-04-21 10:13:21.481162-04	486	Allison Garcy Interiors	1	new through import_export	11	1
41	2025-04-21 10:13:21.481176-04	487	Fritz Advisory	1	new through import_export	11	1
42	2025-04-21 10:13:21.481223-04	488	Amanda Wilkes	1	new through import_export	11	1
43	2025-04-21 10:13:21.481238-04	489	Amanda Mulcahy	1	new through import_export	11	1
44	2025-04-21 10:13:21.481252-04	490	Andrea McCafferty	1	new through import_export	11	1
45	2025-04-21 10:13:21.481267-04	491	Andre Bally	1	new through import_export	11	1
46	2025-04-21 10:13:21.481281-04	492	Felrath Hines LLC	1	new through import_export	11	1
47	2025-04-21 10:13:21.481295-04	493	FOX-NAHEM	1	new through import_export	11	1
48	2025-04-21 10:13:21.481309-04	494	Andrew Pilaro	1	new through import_export	11	1
49	2025-04-21 10:13:21.481324-04	495	The House of Fine Art	1	new through import_export	11	1
50	2025-04-21 10:13:21.481338-04	496	Emphasis Design	1	new through import_export	11	1
51	2025-04-21 10:13:21.481352-04	497	Andy Siegel	1	new through import_export	11	1
52	2025-04-21 10:13:21.481366-04	498	Anna Zorina Gallery	1	new through import_export	11	1
53	2025-04-21 10:13:21.48138-04	499	Berggruen Gallery	1	new through import_export	11	1
54	2025-04-21 10:13:21.481395-04	500	ARC Fine Art LLC	1	new through import_export	11	1
55	2025-04-21 10:13:21.481409-04	501	Hilton Contemporary	1	new through import_export	11	1
56	2025-04-21 10:13:21.481423-04	502	Armann	1	new through import_export	11	1
57	2025-04-21 10:13:21.481437-04	503	White Room Gallery	1	new through import_export	11	1
58	2025-04-21 10:13:21.481451-04	504	April Gornik	1	new through import_export	11	1
59	2025-04-21 10:13:21.481465-04	505	Ashley Masella	1	new through import_export	11	1
60	2025-04-21 10:13:21.481479-04	506	Ashley Stark	1	new through import_export	11	1
61	2025-04-21 10:13:21.481493-04	507	Michelle Gerson Wattell	1	new through import_export	11	1
62	2025-04-21 10:13:21.481507-04	508	Mariska Hargitay	1	new through import_export	11	1
63	2025-04-21 10:13:21.481521-04	509	Audry Casusol	1	new through import_export	11	1
64	2025-04-21 10:13:21.481535-04	510	Axiom Contemporary	1	new through import_export	11	1
65	2025-04-21 10:13:21.481549-04	511	Baboo Imaging Graphics Inc	1	new through import_export	11	1
66	2025-04-21 10:13:21.481563-04	512	Maiken Baird	1	new through import_export	11	1
67	2025-04-21 10:13:21.481577-04	513	Barbara Macklowe	1	new through import_export	11	1
68	2025-04-21 10:13:21.48159-04	514	INGRAO, INC	1	new through import_export	11	1
69	2025-04-21 10:13:21.481604-04	515	Samuel Owen Gallery	1	new through import_export	11	1
70	2025-04-21 10:13:21.481618-04	516	Betsy Mackey	1	new through import_export	11	1
71	2025-04-21 10:13:21.481632-04	517	Tanya Taylor	1	new through import_export	11	1
72	2025-04-21 10:13:21.481646-04	518	Harper's Books	1	new through import_export	11	1
73	2025-04-21 10:13:21.48166-04	519	Blair Dibble	1	new through import_export	11	1
74	2025-04-21 10:13:21.481675-04	520	Bryce Markus	1	new through import_export	11	1
75	2025-04-21 10:13:21.481689-04	521	Robert Fleischer and Katy Glass	1	new through import_export	11	1
76	2025-04-21 10:13:21.481703-04	522	Bob Tabor Images	1	new through import_export	11	1
77	2025-04-21 10:13:21.481718-04	523	Bonnie Lautenberg	1	new through import_export	11	1
78	2025-04-21 10:13:21.481733-04	524	John Hummel	1	new through import_export	11	1
79	2025-04-21 10:13:21.481747-04	525	Brandigall	1	new through import_export	11	1
80	2025-04-21 10:13:21.481762-04	526	Kim Braswell	1	new through import_export	11	1
81	2025-04-21 10:13:21.481775-04	527	Brian Leighton Inc	1	new through import_export	11	1
82	2025-04-21 10:13:21.481789-04	528	Miles McEnery Gallery	1	new through import_export	11	1
83	2025-04-21 10:13:21.481803-04	529	Victoria	1	new through import_export	11	1
84	2025-04-21 10:13:21.481817-04	530	Bonnie Rychlak	1	new through import_export	11	1
85	2025-04-21 10:13:21.481831-04	531	Beth Scharfman	1	new through import_export	11	1
86	2025-04-21 10:13:21.481845-04	532	Budd Goldman	1	new through import_export	11	1
87	2025-04-21 10:13:21.481859-04	533	Goei	1	new through import_export	11	1
88	2025-04-21 10:13:21.481873-04	534	Bjorn Design	1	new through import_export	11	1
89	2025-04-21 10:13:21.481887-04	535	Sandy Robertson	1	new through import_export	11	1
90	2025-04-21 10:13:21.481902-04	536	Carrol Rominoff	1	new through import_export	11	1
91	2025-04-21 10:13:21.481916-04	537	Carola Beeney	1	new through import_export	11	1
92	2025-04-21 10:13:21.48193-04	538	Carol Hunt	1	new through import_export	11	1
93	2025-04-21 10:13:21.481944-04	539	Dekar Design	1	new through import_export	11	1
94	2025-04-21 10:13:21.481958-04	540	FLAG Art Foundation	1	new through import_export	11	1
95	2025-04-21 10:13:21.481976-04	541	Frampton Co	1	new through import_export	11	1
96	2025-04-21 10:13:21.481993-04	542	Cassi Namoda	1	new through import_export	11	1
97	2025-04-21 10:13:21.482008-04	543	ATP.art	1	new through import_export	11	1
98	2025-04-21 10:13:21.482022-04	544	MM Fine Art	1	new through import_export	11	1
99	2025-04-21 10:13:21.482037-04	545	Cathy Glass Design	1	new through import_export	11	1
100	2025-04-21 10:13:21.48205-04	546	Berry Campbell, LLC	1	new through import_export	11	1
101	2025-04-21 10:13:21.482064-04	547	Century Association	1	new through import_export	11	1
102	2025-04-21 10:13:21.482078-04	548	Clic Gallery	1	new through import_export	11	1
103	2025-04-21 10:13:21.482091-04	549	Chandler Smith	1	new through import_export	11	1
104	2025-04-21 10:13:21.482105-04	550	Charlie Ferrer	1	new through import_export	11	1
105	2025-04-21 10:13:21.482118-04	551	Chase Edwards Contemporary	1	new through import_export	11	1
106	2025-04-21 10:13:21.482132-04	552	Karen Kelly	1	new through import_export	11	1
107	2025-04-21 10:13:21.482146-04	553	Cheryl Hazan	1	new through import_export	11	1
108	2025-04-21 10:13:21.482159-04	554	Atelier Purcell	1	new through import_export	11	1
109	2025-04-21 10:13:21.482173-04	555	Audrey Flack	1	new through import_export	11	1
110	2025-04-21 10:13:21.482186-04	556	Chris Hansen	1	new through import_export	11	1
111	2025-04-21 10:13:21.4822-04	557	AWG Art Advisory	1	new through import_export	11	1
112	2025-04-21 10:13:21.482214-04	558	Scott Rudin	1	new through import_export	11	1
113	2025-04-21 10:13:21.482227-04	559	Marjonne	1	new through import_export	11	1
114	2025-04-21 10:13:21.482241-04	560	Cornelia Foss	1	new through import_export	11	1
115	2025-04-21 10:13:21.482254-04	561	DAD Trucking Inc.	1	new through import_export	11	1
116	2025-04-21 10:13:21.482268-04	562	Damien	1	new through import_export	11	1
117	2025-04-21 10:13:21.482282-04	563	Damien Roman Fine Art	1	new through import_export	11	1
118	2025-04-21 10:13:21.482295-04	564	Dan Glaser	1	new through import_export	11	1
119	2025-04-21 10:13:21.482309-04	565	Dana Rubin	1	new through import_export	11	1
120	2025-04-21 10:13:21.482322-04	566	Aetna Fine Art Logistics	1	new through import_export	11	1
121	2025-04-21 10:13:21.482336-04	567	Matthew Marks Gallery	1	new through import_export	11	1
122	2025-04-21 10:13:21.482349-04	568	Dan Nguyen	1	new through import_export	11	1
123	2025-04-21 10:13:21.482363-04	569	David Molner	1	new through import_export	11	1
124	2025-04-21 10:13:21.482377-04	570	David and Sarah Schimmel	1	new through import_export	11	1
125	2025-04-21 10:13:21.48239-04	571	Dawn	1	new through import_export	11	1
126	2025-04-21 10:13:21.482404-04	572	Daniela Carrasco	1	new through import_export	11	1
127	2025-04-21 10:13:21.482418-04	573	Debbie Perlick	1	new through import_export	11	1
128	2025-04-21 10:13:21.482431-04	574	Buck House LLC	1	new through import_export	11	1
129	2025-04-21 10:13:21.482445-04	575	Denise Incandela	1	new through import_export	11	1
130	2025-04-21 10:13:21.482459-04	576	Jasmine Lam	1	new through import_export	11	1
131	2025-04-21 10:13:21.482473-04	577	Dennis Ferrone	1	new through import_export	11	1
132	2025-04-21 10:13:21.482487-04	578	Douglas Maxwell	1	new through import_export	11	1
133	2025-04-21 10:13:21.482501-04	579	Dana Golding	1	new through import_export	11	1
134	2025-04-21 10:13:21.482514-04	580	Steve Diamond	1	new through import_export	11	1
135	2025-04-21 10:13:21.482528-04	581	Margherita Divari	1	new through import_export	11	1
136	2025-04-21 10:13:21.482541-04	582	David Israel	1	new through import_export	11	1
137	2025-04-21 10:13:21.482555-04	583	Affiliated Adjustment Group Ltd.	1	new through import_export	11	1
138	2025-04-21 10:13:21.482573-04	584	Daryl Goldberg-Simon	1	new through import_export	11	1
139	2025-04-21 10:13:21.482587-04	585	Dorian Bergen	1	new through import_export	11	1
140	2025-04-21 10:13:21.4826-04	586	Dream Windows & Interiors, LLC	1	new through import_export	11	1
141	2025-04-21 10:13:21.482614-04	587	Drew Shiflett	1	new through import_export	11	1
142	2025-04-21 10:13:21.482628-04	588	Southampton Art Center	1	new through import_export	11	1
143	2025-04-21 10:13:21.482641-04	589	Duck Creek Arts	1	new through import_export	11	1
144	2025-04-21 10:13:21.482655-04	590	Gregory McKenzie	1	new through import_export	11	1
145	2025-04-21 10:13:21.482669-04	591	Darius Yektai	1	new through import_export	11	1
146	2025-04-21 10:13:21.482682-04	592	Dyektai	1	new through import_export	11	1
147	2025-04-21 10:13:21.482696-04	593	Denny Dimin Gallery	1	new through import_export	11	1
148	2025-04-21 10:13:21.48271-04	594	Elizabeth Bolognino Interiors LLC	1	new through import_export	11	1
149	2025-04-21 10:13:21.482723-04	595	Another Space	1	new through import_export	11	1
150	2025-04-21 10:13:21.482738-04	596	Elliot Cooperstone	1	new through import_export	11	1
151	2025-04-21 10:13:21.482751-04	597	Eleanor Donnelly	1	new through import_export	11	1
152	2025-04-21 10:13:21.482765-04	598	Elissa DeBrito	1	new through import_export	11	1
153	2025-04-21 10:13:21.482778-04	599	Emma DeGennaro	1	new through import_export	11	1
154	2025-04-21 10:13:21.482792-04	600	Judy Gibbons	1	new through import_export	11	1
155	2025-04-21 10:13:21.482805-04	601	Tulla Booth Gallery, LLC	1	new through import_export	11	1
156	2025-04-21 10:13:21.482819-04	602	Elizabeth Hazan	1	new through import_export	11	1
157	2025-04-21 10:13:21.482832-04	603	Eileen Ekstract	1	new through import_export	11	1
158	2025-04-21 10:13:21.482846-04	604	Russell Steel	1	new through import_export	11	1
159	2025-04-21 10:13:21.48286-04	605	Michael John Silverton	1	new through import_export	11	1
160	2025-04-21 10:13:21.482874-04	606	Elephant Designs	1	new through import_export	11	1
161	2025-04-21 10:13:21.482888-04	607	Michael Del Piero Good Design	1	new through import_export	11	1
162	2025-04-21 10:13:21.482903-04	608	Ellen	1	new through import_export	11	1
163	2025-04-21 10:13:21.482916-04	609	John Alschuler	1	new through import_export	11	1
164	2025-04-21 10:13:21.482929-04	610	Emily	1	new through import_export	11	1
165	2025-04-21 10:13:21.482943-04	611	Eric Wuu	1	new through import_export	11	1
166	2025-04-21 10:13:21.482956-04	612	Effie Tstitiridis	1	new through import_export	11	1
167	2025-04-21 10:13:21.48297-04	613	Frank Born	1	new through import_export	11	1
168	2025-04-21 10:13:21.482983-04	614	Eric Fischl	1	new through import_export	11	1
169	2025-04-21 10:13:21.482996-04	615	Open House LTD	1	new through import_export	11	1
170	2025-04-21 10:13:21.48301-04	616	Findlay Galleries	1	new through import_export	11	1
171	2025-04-21 10:13:21.483023-04	617	George Billis Gallery	1	new through import_export	11	1
172	2025-04-21 10:13:21.483037-04	618	Gavin Spanierman	1	new through import_export	11	1
173	2025-04-21 10:13:21.48305-04	619	Gene Bernstein	1	new through import_export	11	1
174	2025-04-21 10:13:21.483064-04	620	Parthenon	1	new through import_export	11	1
175	2025-04-21 10:13:21.483078-04	621	Katherine Gleason	1	new through import_export	11	1
176	2025-04-21 10:13:21.483091-04	622	Kathryn Gleason	1	new through import_export	11	1
177	2025-04-21 10:13:21.483105-04	623	Gayle Lopata	1	new through import_export	11	1
178	2025-04-21 10:13:21.483119-04	624	Gary Moross	1	new through import_export	11	1
179	2025-04-21 10:13:21.483132-04	625	Gianna Putrino	1	new through import_export	11	1
180	2025-04-21 10:13:21.483146-04	626	Rebecca Grafstein	1	new through import_export	11	1
181	2025-04-21 10:13:21.483476-04	627	Greg Carter Studio Management	1	new through import_export	11	1
182	2025-04-21 10:13:21.483501-04	628	Gregory Kong	1	new through import_export	11	1
183	2025-04-21 10:13:21.483515-04	629	Galerie Kornfeld	1	new through import_export	11	1
184	2025-04-21 10:13:21.483528-04	630	Mr. Arslanian	1	new through import_export	11	1
185	2025-04-21 10:13:21.483545-04	631	Venus Over Manhattan	1	new through import_export	11	1
186	2025-04-21 10:13:21.483558-04	632	Adhesivo LLC	1	new through import_export	11	1
187	2025-04-21 10:13:21.483571-04	633	Destination Haus	1	new through import_export	11	1
188	2025-04-21 10:13:21.483585-04	634	Hilary Matt	1	new through import_export	11	1
189	2025-04-21 10:13:21.483598-04	635	Helen Gifford	1	new through import_export	11	1
190	2025-04-21 10:13:21.483612-04	636	Holly Levy	1	new through import_export	11	1
191	2025-04-21 10:13:21.483625-04	637	Hope Rothschild	1	new through import_export	11	1
192	2025-04-21 10:13:21.483638-04	638	Keewaydin Investments	1	new through import_export	11	1
193	2025-04-21 10:13:21.483652-04	639	Heather Sherman	1	new through import_export	11	1
194	2025-04-21 10:13:21.483665-04	640	Claire Oliver Gallery	1	new through import_export	11	1
195	2025-04-21 10:13:21.483679-04	641	Ilene Sands	1	new through import_export	11	1
196	2025-04-21 10:13:21.483692-04	642	Abe Art LLC	1	new through import_export	11	1
197	2025-04-21 10:13:21.483705-04	643	Cavin Morris Gallery	1	new through import_export	11	1
198	2025-04-21 10:13:21.483719-04	644	Plant house	1	new through import_export	11	1
199	2025-04-21 10:13:21.483732-04	645	Rental Gallery	1	new through import_export	11	1
200	2025-04-21 10:13:21.483746-04	646	Cristin Longo	1	new through import_export	11	1
201	2025-04-21 10:13:21.483759-04	647	Sponder Gallery	1	new through import_export	11	1
202	2025-04-21 10:13:21.483773-04	648	Intense Movers	1	new through import_export	11	1
203	2025-04-21 10:13:21.483787-04	649	Irina Alimanestianu	1	new through import_export	11	1
204	2025-04-21 10:13:21.483801-04	650	Irving Grauer	1	new through import_export	11	1
205	2025-04-21 10:13:21.483815-04	651	Isaac Reynoso	1	new through import_export	11	1
206	2025-04-21 10:13:21.483828-04	652	Inplus Inc.	1	new through import_export	11	1
207	2025-04-21 10:13:21.483842-04	653	Jessica VonHagn	1	new through import_export	11	1
208	2025-04-21 10:13:21.483855-04	654	Jackie Paolone	1	new through import_export	11	1
209	2025-04-21 10:13:21.483869-04	655	James DeMartis Metal Studio	1	new through import_export	11	1
210	2025-04-21 10:13:21.483882-04	656	McAlpine House	1	new through import_export	11	1
211	2025-04-21 10:13:21.483896-04	657	Janet Jennings	1	new through import_export	11	1
212	2025-04-21 10:13:21.483909-04	658	Janet Lehr	1	new through import_export	11	1
213	2025-04-21 10:13:21.483922-04	659	Joseph Bell	1	new through import_export	11	1
214	2025-04-21 10:13:21.483936-04	660	Jay Bialsky	1	new through import_export	11	1
215	2025-04-21 10:13:21.48395-04	661	Natalie	1	new through import_export	11	1
216	2025-04-21 10:13:21.483963-04	662	J Design Group	1	new through import_export	11	1
217	2025-04-21 10:13:21.483976-04	663	Jean Albano Gallery	1	new through import_export	11	1
218	2025-04-21 10:13:21.48399-04	664	Jeff Lincoln	1	new through import_export	11	1
219	2025-04-21 10:13:21.484003-04	665	Jen Going Interiors JDG	1	new through import_export	11	1
220	2025-04-21 10:13:21.484017-04	666	Jessica Cohen Designs	1	new through import_export	11	1
221	2025-04-21 10:13:21.48403-04	667	Jessica Lichtenstein	1	new through import_export	11	1
222	2025-04-21 10:13:21.484044-04	668	Jonathan Grayer	1	new through import_export	11	1
223	2025-04-21 10:13:21.484057-04	669	Jennifer Whitman	1	new through import_export	11	1
224	2025-04-21 10:13:21.48407-04	670	Jim Daiyle	1	new through import_export	11	1
225	2025-04-21 10:13:21.484084-04	671	The American Academy of Arts & Letters	1	new through import_export	11	1
226	2025-04-21 10:13:21.484097-04	672	Carvalho Park Gallery	1	new through import_export	11	1
227	2025-04-21 10:13:21.484111-04	673	Cromwell Art	1	new through import_export	11	1
228	2025-04-21 10:13:21.484124-04	674	Jeff Muhs	1	new through import_export	11	1
229	2025-04-21 10:13:21.484137-04	675	High Fashion Concepts	1	new through import_export	11	1
230	2025-04-21 10:13:21.484151-04	676	Joanna	1	new through import_export	11	1
231	2025-04-21 10:13:21.484164-04	677	Joanne Carson Art Studio	1	new through import_export	11	1
232	2025-04-21 10:13:21.484178-04	678	Joanne Greenbaum	1	new through import_export	11	1
233	2025-04-21 10:13:21.484191-04	679	Paula Cooper Gallery	1	new through import_export	11	1
234	2025-04-21 10:13:21.484206-04	680	Joel Mesler	1	new through import_export	11	1
235	2025-04-21 10:13:21.484219-04	681	John Picker	1	new through import_export	11	1
236	2025-04-21 10:13:21.484232-04	682	John Alexander	1	new through import_export	11	1
237	2025-04-21 10:13:21.484246-04	683	John Acierno	1	new through import_export	11	1
238	2025-04-21 10:13:21.484259-04	684	Jonathan Boos	1	new through import_export	11	1
239	2025-04-21 10:13:21.484272-04	685	Kathy Kuo Home	1	new through import_export	11	1
240	2025-04-21 10:13:21.484286-04	686	Josef Najar	1	new through import_export	11	1
241	2025-04-21 10:13:21.484299-04	687	Jennifer Gardner	1	new through import_export	11	1
242	2025-04-21 10:13:21.484312-04	688	C and C Gallery	1	new through import_export	11	1
243	2025-04-21 10:13:21.484325-04	689	Rebecca Hossack Gallery	1	new through import_export	11	1
244	2025-04-21 10:13:21.484339-04	690	One Main (The BZZAAR Inc.)	1	new through import_export	11	1
245	2025-04-21 10:13:21.484353-04	691	Keyes Art Gallery	1	new through import_export	11	1
246	2025-04-21 10:13:21.484366-04	692	Kai Gallery LLC	1	new through import_export	11	1
247	2025-04-21 10:13:21.484379-04	693	Agora Gallery	1	new through import_export	11	1
248	2025-04-21 10:13:21.484418-04	694	Jutta Kraus	1	new through import_export	11	1
249	2025-04-21 10:13:21.484437-04	695	Juvy Miraflor	1	new through import_export	11	1
250	2025-04-21 10:13:21.484451-04	696	Joan Holden	1	new through import_export	11	1
251	2025-04-21 10:13:21.484464-04	697	Joe Farrell	1	new through import_export	11	1
252	2025-04-21 10:13:21.484478-04	698	Catalyst Art	1	new through import_export	11	1
253	2025-04-21 10:13:21.484491-04	699	Susana Simonpietri	1	new through import_export	11	1
254	2025-04-21 10:13:21.484505-04	700	Eric Firestone Gallery	1	new through import_export	11	1
255	2025-04-21 10:13:21.484518-04	701	Contessa Gallery	1	new through import_export	11	1
256	2025-04-21 10:13:21.484531-04	702	Elements In Play	1	new through import_export	11	1
257	2025-04-21 10:13:21.484545-04	703	Hesse Flatow LLC	1	new through import_export	11	1
258	2025-04-21 10:13:21.484559-04	704	Bonhams New York	1	new through import_export	11	1
259	2025-04-21 10:13:21.484572-04	705	Long House Reserve	1	new through import_export	11	1
260	2025-04-21 10:13:21.484586-04	706	Hauser & Wirth	1	new through import_export	11	1
261	2025-04-21 10:13:21.484599-04	707	Katie Lydon Interiors	1	new through import_export	11	1
262	2025-04-21 10:13:21.484613-04	708	KMR Arts	1	new through import_export	11	1
263	2025-04-21 10:13:21.484626-04	709	Kathy Markel	1	new through import_export	11	1
264	2025-04-21 10:13:21.48464-04	710	Karen Bromberg	1	new through import_export	11	1
265	2025-04-21 10:13:21.484653-04	711	Cultural Counsel	1	new through import_export	11	1
266	2025-04-21 10:13:21.484667-04	712	Kelli Hull	1	new through import_export	11	1
267	2025-04-21 10:13:21.48468-04	713	Kelly & Henry Prince	1	new through import_export	11	1
268	2025-04-21 10:13:21.484694-04	714	Katie Leede	1	new through import_export	11	1
269	2025-04-21 10:13:21.484707-04	715	Dominick Rotondi	1	new through import_export	11	1
270	2025-04-21 10:13:21.484721-04	716	Kevin Hart	1	new through import_export	11	1
271	2025-04-21 10:13:21.484735-04	717	Khim Davis	1	new through import_export	11	1
272	2025-04-21 10:13:21.484748-04	718	James Cohan Gallery	1	new through import_export	11	1
273	2025-04-21 10:13:21.484762-04	719	Parrish Art Museum	1	new through import_export	11	1
274	2025-04-21 10:13:21.484775-04	720	Mike Schneider	1	new through import_export	11	1
275	2025-04-21 10:13:21.484789-04	721	Montauk Yacht Club	1	new through import_export	11	1
276	2025-04-21 10:13:21.484802-04	722	Kramoris Gallery	1	new through import_export	11	1
277	2025-04-21 10:13:21.484816-04	723	Francoise Ghebaly	1	new through import_export	11	1
278	2025-04-21 10:13:21.48483-04	724	Kimberly Yoon	1	new through import_export	11	1
279	2025-04-21 10:13:21.484843-04	725	Larry Kane	1	new through import_export	11	1
280	2025-04-21 10:13:21.484857-04	726	Laura Solomon	1	new through import_export	11	1
281	2025-04-21 10:13:21.48487-04	727	Joline Stemerman	1	new through import_export	11	1
282	2025-04-21 10:13:21.484884-04	728	Laurence	1	new through import_export	11	1
283	2025-04-21 10:13:21.484897-04	729	Linda Burkhardt	1	new through import_export	11	1
284	2025-04-21 10:13:21.484911-04	730	Lisa Guida	1	new through import_export	11	1
285	2025-04-21 10:13:21.484924-04	731	Leslie Ghize	1	new through import_export	11	1
286	2025-04-21 10:13:21.484938-04	732	The Noguchi Museum	1	new through import_export	11	1
287	2025-04-21 10:13:21.484951-04	733	Lilly Bunn	1	new through import_export	11	1
288	2025-04-21 10:13:21.484964-04	734	Linda J Sirow	1	new through import_export	11	1
289	2025-04-21 10:13:21.484978-04	735	Nino Mier Gallery	1	new through import_export	11	1
290	2025-04-21 10:13:21.484991-04	736	Kemble Interiors	1	new through import_export	11	1
291	2025-04-21 10:13:21.485004-04	737	Liz Vayner	1	new through import_export	11	1
292	2025-04-21 10:13:21.485018-04	738	Lisa Marie Milat	1	new through import_export	11	1
293	2025-04-21 10:13:21.485031-04	739	Lochen Design	1	new through import_export	11	1
294	2025-04-21 10:13:21.485045-04	740	Louise P. Sloane	1	new through import_export	11	1
295	2025-04-21 10:13:21.485058-04	741	Lani Shufelt	1	new through import_export	11	1
296	2025-04-21 10:13:21.485071-04	742	Laura Traphagen	1	new through import_export	11	1
297	2025-04-21 10:13:21.485085-04	743	Lynn Savarese	1	new through import_export	11	1
298	2025-04-21 10:13:21.485098-04	744	Lynn Avenue, LLC.	1	new through import_export	11	1
299	2025-04-21 10:13:21.485112-04	745	Laurie Zucker	1	new through import_export	11	1
300	2025-04-21 10:13:21.485125-04	746	Maggie Tolkin	1	new through import_export	11	1
301	2025-04-21 10:13:21.485139-04	747	Michael Altman	1	new through import_export	11	1
302	2025-04-21 10:13:21.485152-04	748	Pure Art Services	1	new through import_export	11	1
303	2025-04-21 10:13:21.485166-04	749	The Selects Gallery	1	new through import_export	11	1
304	2025-04-21 10:13:21.48518-04	750	Embed Creative	1	new through import_export	11	1
305	2025-04-21 10:13:21.485193-04	751	Katja Goldman	1	new through import_export	11	1
306	2025-04-21 10:13:21.485206-04	752	Mayrock Art	1	new through import_export	11	1
307	2025-04-21 10:13:21.48522-04	753	Serena & Lily	1	new through import_export	11	1
308	2025-04-21 10:13:21.485233-04	754	Building Details	1	new through import_export	11	1
309	2025-04-21 10:13:21.485246-04	755	Nicole Klagsbrun Inc	1	new through import_export	11	1
310	2025-04-21 10:13:21.48526-04	756	Vallarino Fine Art	1	new through import_export	11	1
311	2025-04-21 10:13:21.485274-04	757	Matt Shamnoski	1	new through import_export	11	1
312	2025-04-21 10:13:21.485287-04	758	Dietl	1	new through import_export	11	1
313	2025-04-21 10:13:21.485301-04	759	Michael Aviles	1	new through import_export	11	1
314	2025-04-21 10:13:21.485314-04	760	Darrow Contemporary	1	new through import_export	11	1
315	2025-04-21 10:13:21.485327-04	761	Sean McCarthy	1	new through import_export	11	1
316	2025-04-21 10:13:21.485341-04	762	Leyden Lewis	1	new through import_export	11	1
317	2025-04-21 10:13:21.485355-04	763	Miles Jaffee	1	new through import_export	11	1
318	2025-04-21 10:13:21.485369-04	764	Max Dolgicer	1	new through import_export	11	1
319	2025-04-21 10:13:21.485382-04	765	Grenning Gallery	1	new through import_export	11	1
320	2025-04-21 10:13:21.485414-04	766	Megan Riley	1	new through import_export	11	1
321	2025-04-21 10:13:21.485428-04	767	Brian J. McCarthy	1	new through import_export	11	1
322	2025-04-21 10:13:21.485445-04	768	Markt Art Advisory	1	new through import_export	11	1
323	2025-04-21 10:13:21.485458-04	769	Meredith Keay	1	new through import_export	11	1
324	2025-04-21 10:13:21.485471-04	770	MFS Sculpture Jewelry	1	new through import_export	11	1
325	2025-04-21 10:13:21.485485-04	771	Michal Mufson	1	new through import_export	11	1
326	2025-04-21 10:13:21.485498-04	772	Nicole Brady	1	new through import_export	11	1
327	2025-04-21 10:13:21.485512-04	773	Sag Harbor Cinema	1	new through import_export	11	1
328	2025-04-21 10:13:21.485525-04	774	Mindy & Daniel Bass	1	new through import_export	11	1
329	2025-04-21 10:13:21.485539-04	775	Miriam	1	new through import_export	11	1
330	2025-04-21 10:13:21.485553-04	776	Marie Josée Primeau	1	new through import_export	11	1
331	2025-04-21 10:13:21.485566-04	777	Mickey Baumrind	1	new through import_export	11	1
332	2025-04-21 10:13:21.48558-04	778	Marty Melzer	1	new through import_export	11	1
333	2025-04-21 10:13:21.485593-04	779	New York Academy of Art	1	new through import_export	11	1
334	2025-04-21 10:13:21.485607-04	780	Meryl Taradash	1	new through import_export	11	1
335	2025-04-21 10:13:21.48562-04	781	Mike Chutko	1	new through import_export	11	1
336	2025-04-21 10:13:21.485633-04	782	Mary Weatherford Inc.	1	new through import_export	11	1
337	2025-04-21 10:13:21.485647-04	783	Nadia Anderson	1	new through import_export	11	1
338	2025-04-21 10:13:21.48566-04	784	Mark Lehr	1	new through import_export	11	1
339	2025-04-21 10:13:21.485673-04	785	Nancy Larsen	1	new through import_export	11	1
340	2025-04-21 10:13:21.485687-04	786	Marc Leder	1	new through import_export	11	1
341	2025-04-21 10:13:21.4857-04	787	Casterline Goodman Gallery	1	new through import_export	11	1
342	2025-04-21 10:13:21.485713-04	788	Natalie Antoine	1	new through import_export	11	1
343	2025-04-21 10:13:21.485727-04	789	Nick Dietz	1	new through import_export	11	1
344	2025-04-21 10:13:21.48574-04	790	Hidden Lake Asset Management	1	new through import_export	11	1
345	2025-04-21 10:13:21.485754-04	791	Paul. Davis	1	new through import_export	11	1
346	2025-04-21 10:13:21.485768-04	792	Nikki Brown	1	new through import_export	11	1
347	2025-04-21 10:13:21.485783-04	793	Samuels Creative & Co.	1	new through import_export	11	1
348	2025-04-21 10:13:21.485797-04	794	Norman Weisfeld	1	new through import_export	11	1
349	2025-04-21 10:13:21.48581-04	795	Nathan Strieter	1	new through import_export	11	1
350	2025-04-21 10:13:21.485824-04	796	Corder Management	1	new through import_export	11	1
351	2025-04-21 10:13:21.485837-04	797	Dan Hasted	1	new through import_export	11	1
352	2025-04-21 10:13:21.48585-04	798	Oscar Junquera	1	new through import_export	11	1
353	2025-04-21 10:13:21.485864-04	799	Omar Baker	1	new through import_export	11	1
354	2025-04-21 10:13:21.485877-04	800	Phillip Danisi	1	new through import_export	11	1
355	2025-04-21 10:13:21.485891-04	801	Patricia McGrath Design	1	new through import_export	11	1
356	2025-04-21 10:13:21.485904-04	802	Michael Davis	1	new through import_export	11	1
357	2025-04-21 10:13:21.485917-04	803	Patrick Creedon	1	new through import_export	11	1
358	2025-04-21 10:13:21.485931-04	804	Clifford Ross	1	new through import_export	11	1
359	2025-04-21 10:13:21.485944-04	805	Paul Davis	1	new through import_export	11	1
360	2025-04-21 10:13:21.485957-04	806	Peter Buchman	1	new through import_export	11	1
361	2025-04-21 10:13:21.485971-04	807	Guild Hall East Hampton	1	new through import_export	11	1
362	2025-04-21 10:13:21.485984-04	808	Perry Steiner	1	new through import_export	11	1
363	2025-04-21 10:13:21.485998-04	809	Peter Dayton LLC	1	new through import_export	11	1
364	2025-04-21 10:13:21.486011-04	810	Peter Simon	1	new through import_export	11	1
365	2025-04-21 10:13:21.486024-04	811	Peter Genatt	1	new through import_export	11	1
366	2025-04-21 10:13:21.486038-04	812	Blond Contemporary	1	new through import_export	11	1
367	2025-04-21 10:13:21.486051-04	813	Mark Borghi Fine Art Inc.	1	new through import_export	11	1
368	2025-04-21 10:13:21.486064-04	814	Peter Lee	1	new through import_export	11	1
369	2025-04-21 10:13:21.486079-04	815	Benrubi Gallery	1	new through import_export	11	1
370	2025-04-21 10:13:21.486093-04	816	Tina Kim Gallery	1	new through import_export	11	1
371	2025-04-21 10:13:21.486106-04	817	Robert Guida	1	new through import_export	11	1
372	2025-04-21 10:13:21.48612-04	818	Randi Ball	1	new through import_export	11	1
373	2025-04-21 10:13:21.486133-04	819	Rebecca Homapour	1	new through import_export	11	1
374	2025-04-21 10:13:21.486146-04	820	Robin Matza Design	1	new through import_export	11	1
375	2025-04-21 10:13:21.48616-04	821	Peggy Gelfond	1	new through import_export	11	1
376	2025-04-21 10:13:21.486173-04	822	Richard Rothschild	1	new through import_export	11	1
377	2025-04-21 10:13:21.486186-04	823	Richard Friedman	1	new through import_export	11	1
378	2025-04-21 10:13:21.4862-04	824	Dan Rizzie	1	new through import_export	11	1
379	2025-04-21 10:13:21.486213-04	825	Front Desk Apparatus	1	new through import_export	11	1
380	2025-04-21 10:13:21.486227-04	826	Pie Pie MTK LLC	1	new through import_export	11	1
381	2025-04-21 10:13:21.48624-04	827	University of Lynchburg	1	new through import_export	11	1
382	2025-04-21 10:13:21.486253-04	828	Colm Rowan Fine Art	1	new through import_export	11	1
383	2025-04-21 10:13:21.486267-04	829	By Appointment Hamptons	1	new through import_export	11	1
384	2025-04-21 10:13:21.48628-04	830	I.V. Contemporary LLC	1	new through import_export	11	1
385	2025-04-21 10:13:21.486294-04	831	Brooke Abrams Design	1	new through import_export	11	1
386	2025-04-21 10:13:21.486307-04	832	Nightingale Gallery	1	new through import_export	11	1
387	2025-04-21 10:13:21.48632-04	833	Sears-Peyton Gallery	1	new through import_export	11	1
388	2025-04-21 10:13:21.486334-04	834	The Journal Gallery	1	new through import_export	11	1
389	2025-04-21 10:13:21.486347-04	835	Susanna Adler	1	new through import_export	11	1
390	2025-04-21 10:13:21.48636-04	836	Michael Schubert	1	new through import_export	11	1
391	2025-04-21 10:13:21.486374-04	837	Roy Seifert	1	new through import_export	11	1
392	2025-04-21 10:13:21.486387-04	838	Sara Fitzmaurice	1	new through import_export	11	1
393	2025-04-21 10:13:21.486401-04	839	Mitchell-Innes & Nash, Inc.	1	new through import_export	11	1
394	2025-04-21 10:13:21.486414-04	840	Sheri Sandler	1	new through import_export	11	1
395	2025-04-21 10:13:21.486427-04	841	Michael Weinberg	1	new through import_export	11	1
396	2025-04-21 10:13:21.486441-04	842	The Church Sag Harbor	1	new through import_export	11	1
397	2025-04-21 10:13:21.486454-04	843	Susan Kane	1	new through import_export	11	1
398	2025-04-21 10:13:21.486469-04	844	Shawn Levy	1	new through import_export	11	1
399	2025-04-21 10:13:21.486482-04	845	Swann Auction Galleries	1	new through import_export	11	1
400	2025-04-21 10:13:21.486496-04	846	Sloan Schaffer	1	new through import_export	11	1
401	2025-04-21 10:13:21.486509-04	847	David Scott	1	new through import_export	11	1
402	2025-04-21 10:13:21.486523-04	848	Sloane Hubbuch	1	new through import_export	11	1
403	2025-04-21 10:13:21.486536-04	849	Sylvia Oberwager	1	new through import_export	11	1
404	2025-04-21 10:13:21.48655-04	850	Steve Cohn	1	new through import_export	11	1
405	2025-04-21 10:13:21.486563-04	851	Hollis Taggart	1	new through import_export	11	1
406	2025-04-21 10:13:21.486576-04	852	Eli Wilner & Co. INC	1	new through import_export	11	1
407	2025-04-21 10:13:21.48659-04	853	MARIANNE BOESKY GALLERY	1	new through import_export	11	1
408	2025-04-21 10:13:21.486603-04	854	Stafford Broumand	1	new through import_export	11	1
409	2025-04-21 10:13:21.486616-04	855	Stefani Shavel	1	new through import_export	11	1
410	2025-04-21 10:13:21.48663-04	856	Julie Stelzer	1	new through import_export	11	1
411	2025-04-21 10:13:21.486643-04	857	Allan Schwartzman	1	new through import_export	11	1
412	2025-04-21 10:13:21.486656-04	858	Steve Rabin	1	new through import_export	11	1
413	2025-04-21 10:13:21.48667-04	859	Stewart Gross	1	new through import_export	11	1
414	2025-04-21 10:13:21.486684-04	860	Stuart Rothstein	1	new through import_export	11	1
415	2025-04-21 10:13:21.486697-04	861	DFI Services / Adco Group	1	new through import_export	11	1
416	2025-04-21 10:13:21.48671-04	862	Sue Ball	1	new through import_export	11	1
417	2025-04-21 10:13:21.486724-04	863	N 53 Gallery	1	new through import_export	11	1
418	2025-04-21 10:13:21.486737-04	864	Caldwell Snyder	1	new through import_export	11	1
419	2025-04-21 10:13:21.48675-04	865	Susan Gross	1	new through import_export	11	1
420	2025-04-21 10:13:21.486764-04	866	North Shore Cosmetic	1	new through import_export	11	1
421	2025-04-21 10:13:21.486777-04	867	Suzanne Anker	1	new through import_export	11	1
422	2025-04-21 10:13:21.48679-04	868	Lori Margolis Interiors	1	new through import_export	11	1
423	2025-04-21 10:13:21.486804-04	869	S Bitter-Larkin Fine Art Inc.	1	new through import_export	11	1
424	2025-04-21 10:13:21.486817-04	870	Stephen Zaro	1	new through import_export	11	1
425	2025-04-21 10:13:21.48683-04	871	Christine Blaustein	1	new through import_export	11	1
426	2025-04-21 10:13:21.486843-04	872	Suffolk Community College Association Inc.	1	new through import_export	11	1
427	2025-04-21 10:13:21.486857-04	873	Terri Hyland	1	new through import_export	11	1
428	2025-04-21 10:13:21.48687-04	874	Theodore Rojos	1	new through import_export	11	1
429	2025-04-21 10:13:21.486883-04	875	Espinasse31 INC	1	new through import_export	11	1
430	2025-04-21 10:13:21.486897-04	876	Mary Ryan Gallery	1	new through import_export	11	1
431	2025-04-21 10:13:21.48691-04	877	Ryan Lee Gallery	1	new through import_export	11	1
432	2025-04-21 10:13:21.486924-04	878	Thomas Gleeson	1	new through import_export	11	1
433	2025-04-21 10:13:21.486937-04	879	Yarger Fine Art	1	new through import_export	11	1
434	2025-04-21 10:13:21.48695-04	880	Tim O'Conner	1	new through import_export	11	1
435	2025-04-21 10:13:21.486965-04	881	Bay Street	1	new through import_export	11	1
436	2025-04-21 10:13:21.486978-04	882	Buckner Projects	1	new through import_export	11	1
437	2025-04-21 10:13:21.486992-04	883	David Nolan Gallery	1	new through import_export	11	1
438	2025-04-21 10:13:21.487005-04	884	Mckenzie Fine Art	1	new through import_export	11	1
439	2025-04-21 10:13:21.487069-04	885	Vered Art	1	new through import_export	11	1
440	2025-04-21 10:13:21.487083-04	886	Victoria Katsov	1	new through import_export	11	1
441	2025-04-21 10:13:21.487097-04	887	Turnberry	1	new through import_export	11	1
442	2025-04-21 10:13:21.48711-04	888	Ocean Graphics	1	new through import_export	11	1
443	2025-04-21 10:13:21.487124-04	889	Juanita Wimberley	1	new through import_export	11	1
444	2025-04-21 10:13:21.487137-04	890	Morrison Gallery	1	new through import_export	11	1
445	2025-04-21 10:13:21.487151-04	891	Wendy Frieder	1	new through import_export	11	1
446	2025-04-21 10:13:21.487164-04	892	Yanina Fuertes	1	new through import_export	11	1
447	2025-04-21 10:33:30.694084-04	1	ejartmover@gmail.com	1	[{"added": {}}]	3	1
448	2025-04-21 10:34:16.051204-04	2	ejartmover@gmail.com	1	[{"added": {}}]	6	1
449	2025-04-21 10:34:33.461287-04	2	ejartmover@gmail.com	2	[]	6	1
450	2025-04-21 10:35:42.68834-04	2	ejartmover@gmail.com	2	[{"changed": {"fields": ["User permissions"]}}]	6	1
463	2025-05-07 13:05:20.355358-04	34	josicki0704@gmail.com	1	[{"added": {}}]	6	1
464	2025-05-07 13:06:02.987816-04	34	josicki0704@gmail.com	2	[{"changed": {"fields": ["User permissions"]}}]	6	1
496	2025-05-11 16:59:22.743045-04	67	Stacy.a.gorman@gmail.com	1	[{"added": {}}]	6	1
497	2025-05-11 17:00:25.702872-04	67	Stacy.a.gorman@gmail.com	2	[{"changed": {"fields": ["User permissions"]}}]	6	1
498	2025-05-11 17:01:25.167478-04	34	josicki0704@gmail.com	2	[{"changed": {"fields": ["User permissions"]}}]	6	1
499	2025-05-12 18:24:34.350829-04	67	stacy.a.gorman@gmail.com	2	[{"changed": {"fields": ["Email address", "Username"]}}]	6	1
500	2025-05-14 14:59:21.092024-04	100	bblueheron@gmail.com	1	[{"added": {}}]	6	1
501	2025-05-14 15:00:00.910551-04	100	bblueheron@gmail.com	2	[{"changed": {"fields": ["User permissions"]}}]	6	1
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2025-04-19 19:25:48.204183-04
2	contenttypes	0002_remove_content_type_name	2025-04-19 19:25:48.212886-04
3	auth	0001_initial	2025-04-19 19:25:48.301038-04
4	auth	0002_alter_permission_name_max_length	2025-04-19 19:25:48.307359-04
5	auth	0003_alter_user_email_max_length	2025-04-19 19:25:48.313053-04
6	auth	0004_alter_user_username_opts	2025-04-19 19:25:48.319006-04
7	auth	0005_alter_user_last_login_null	2025-04-19 19:25:48.325136-04
8	auth	0006_require_contenttypes_0002	2025-04-19 19:25:48.328376-04
9	auth	0007_alter_validators_add_error_messages	2025-04-19 19:25:48.334283-04
10	auth	0008_alter_user_username_max_length	2025-04-19 19:25:48.343694-04
11	auth	0009_alter_user_last_name_max_length	2025-04-19 19:25:48.355082-04
12	auth	0010_alter_group_name_max_length	2025-04-19 19:25:48.36373-04
13	auth	0011_update_proxy_permissions	2025-04-19 19:25:48.370887-04
14	auth	0012_alter_user_first_name_max_length	2025-04-19 19:25:48.376918-04
15	accounts	0001_initial	2025-04-19 19:25:48.490164-04
16	admin	0001_initial	2025-04-19 19:25:48.531266-04
17	admin	0002_logentry_remove_auto_add	2025-04-19 19:25:48.53844-04
18	admin	0003_logentry_add_action_flag_choices	2025-04-19 19:25:48.54603-04
19	clients	0001_initial	2025-04-19 19:25:48.573429-04
20	workorders	0001_initial	2025-04-19 19:25:48.678219-04
21	invoices	0001_initial	2025-04-19 19:25:48.735819-04
22	sessions	0001_initial	2025-04-19 19:25:48.770233-04
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
wg35abh2vemwmt5cgk8w3hd3r8mancy5	.eJxVjEEOwiAQRe_C2hBBKIxL9z0DGWYmUjWQlHZlvLtt0oVu_3vvv1XCdSlp7TKnidVVGXX63TLSU-oO-IH13jS1usxT1ruiD9r12Fhet8P9OyjYy1Z7IPDsLOXBWwz27BhiJCdgvYNs-SIIQ_CBggQCsRs3ECJ6ZBMR1OcLzbE3cA:1u6HkM:ZRAFW1g-bAEj3skYLLJEnxEb5dMHCmArsOAJ5iOyvgc	2025-05-03 19:37:18.94407-04
jqpnljs5ji1kc1pyer51yw01xd1nlf4o	.eJxVjEEOwiAQRe_C2hBBKIxL9z0DGWYmUjWQlHZlvLtt0oVu_3vvv1XCdSlp7TKnidVVGXX63TLSU-oO-IH13jS1usxT1ruiD9r12Fhet8P9OyjYy1Z7IPDsLOXBWwz27BhiJCdgvYNs-SIIQ_CBggQCsRs3ECJ6ZBMR1OcLzbE3cA:1u848F:N46wigpL1vPjTLH-07DXNAFFZ0fxpkAosAiQIm2LC_I	2025-05-08 17:29:19.465068-04
mnst8d4f9cgjy70hfl07gx8s8n0uzlfe	.eJxVjMsOwiAURP-FtSHyaCku3fsNBO5DqgaS0q6M_25JutBZzpwzbxHituawNVrCjOIitDj9dinCk0of8BHLvUqoZV3mJDsij7XJW0V6XQ_27yDHlneb2Dqw5mwYEZRjpQiRFbsBkIzXFsYJvAfkTuKA055kdkGPYGMSny8RBDjZ:1u86zZ:hEOb2l4Dc1QmCStqiUMEKfg9QAERMLqKCAs8yp55btw	2025-05-08 20:32:33.100146-04
vt769znn7kt3ptzmjotzdouybolpr2ei	.eJxVjMsOwiAURP-FtSHyaCku3fsNBO5DqgaS0q6M_25JutBZzpwzbxHituawNVrCjOIitDj9dinCk0of8BHLvUqoZV3mJDsij7XJW0V6XQ_27yDHlneb2Dqw5mwYEZRjpQiRFbsBkIzXFsYJvAfkTuKA055kdkGPYGMSny8RBDjZ:1uCG9V:1DY9pe4A8miEvzzMNNhF46_onaUBd90TE2x1_aHYb_4	2025-05-20 07:07:57.329656-04
2tv2czr19igebuw0gaa7nvawr9x4jw3o	.eJxVjMsOwiAURP-FtSHyaCku3fsNBO5DqgaS0q6M_25JutBZzpwzbxHituawNVrCjOIitDj9dinCk0of8BHLvUqoZV3mJDsij7XJW0V6XQ_27yDHlneb2Dqw5mwYEZRjpQiRFbsBkIzXFsYJvAfkTuKA055kdkGPYGMSny8RBDjZ:1uCRyw:AJcrqpK96L0ghooEQ4XSCIhzVmQ5nb6H-GCB_I4FkV8	2025-05-20 19:45:50.455287-04
ev1i6l6fne2uho5dulg87c0mci6p6grz	.eJxVjEEOwiAQAP_C2ZBSKHQ9eu8byLK72KqBpLQn499Nkx70OjOZt4q4b3Pcm6xxYXVV1qnLL0xITymH4QeWe9VUy7YuSR-JPm3TU2V53c72bzBjm48vWs-Cph-DyR5CZ3mQzvejZ2KfwRG6AIPJiYCyk9CNFhIFk5wRsKA-XwOEN_E:1uCp2A:QYM5qUS65zB5Xu50c2npT4edPEkoN-GXj6gXjJigLYY	2025-05-21 20:22:42.394996-04
ponr0pnx55v97u834pghmq327blvvvy4	.eJxVjMsOwiAURP-FtSHyaCku3fsNBO5DqgaS0q6M_25JutBZzpwzbxHituawNVrCjOIitDj9dinCk0of8BHLvUqoZV3mJDsij7XJW0V6XQ_27yDHlneb2Dqw5mwYEZRjpQiRFbsBkIzXFsYJvAfkTuKA055kdkGPYGMSny8RBDjZ:1uDMJg:Y42qzdz6r5phK-VyMrAsdu6PtPxuFmAdKKAiDIzYC1I	2025-05-23 07:55:00.484832-04
x7lw908hj9rfp8iiy3racgsb2zun4wwk	.eJxVjEEOwiAQRe_C2hBBKIxL9z0DGWYmUjWQlHZlvLtt0oVu_3vvv1XCdSlp7TKnidVVGXX63TLSU-oO-IH13jS1usxT1ruiD9r12Fhet8P9OyjYy1Z7IPDsLOXBWwz27BhiJCdgvYNs-SIIQ_CBggQCsRs3ECJ6ZBMR1OcLzbE3cA:1uDR1p:aKakEDBrivTak40NLCRlugPMufVUy4Vp0RnCBXZDtTA	2025-05-23 12:56:53.405666-04
2xcb2pp8tta2vwb86pjwi6qnzs9vgkjr	.eJxVjMsOwiAURP-FtSHyaCku3fsNBO5DqgaS0q6M_25JutBZzpwzbxHituawNVrCjOIitDj9dinCk0of8BHLvUqoZV3mJDsij7XJW0V6XQ_27yDHlneb2Dqw5mwYEZRjpQiRFbsBkIzXFsYJvAfkTuKA055kdkGPYGMSny8RBDjZ:1uEbN6:GBPfIsu5pkUKQ4R3EY4mQ7M_8G1YZ5QG2V2YPXTBZnM	2025-05-26 18:11:40.735934-04
77c8jf2ebqui5qx7afz9ih4o223t2d9a	.eJxVjEEOwiAQRe_C2hBBKIxL9z0DGWYmUjWQlHZlvLtt0oVu_3vvv1XCdSlp7TKnidVVGXX63TLSU-oO-IH13jS1usxT1ruiD9r12Fhet8P9OyjYy1Z7IPDsLOXBWwz27BhiJCdgvYNs-SIIQ_CBggQCsRs3ECJ6ZBMR1OcLzbE3cA:1uFHSt:jbAiAtmDcLSBqVk9-9vOpuzcHFcB1YFkOmZ2GDS7gg8	2025-05-28 15:08:27.759369-04
qr78g3rz17p0f0bwkb614i0li2ly4dam	.eJxVjDEOgzAMRe-SuYpiHKKkY_eeATm2KbRVkAhMqHcvSAzt-t97fzMdrcvQrVXnbhRzNeCcufyumfil5UDypPKYLE9lmcdsD8WetNr7JPq-ne7fwUB12GsWQu5z0-cUEwLHNrikMQmSYCRw0LBwDskjQMrBa0CPLULf7lZU8_kCOl84EQ:1uFHTk:QztVR2rXs9Q38e5vMv8_sWDXHTyoAxyC_m3TxetuFGE	2025-05-28 15:09:20.223038-04
4s5hb0f7jzj1vqdq3xmv5jduyzrgzy9n	.eJxVjDEOgzAMRe-SuYpiHKKkY_eeATm2KbRVkAhMqHcvSAzt-t97fzMdrcvQrVXnbhRzNeCcufyumfil5UDypPKYLE9lmcdsD8WetNr7JPq-ne7fwUB12GsWQu5z0-cUEwLHNrikMQmSYCRw0LBwDskjQMrBa0CPLULf7lZU8_kCOl84EQ:1uFHoo:ooMWa2jMOBMP0mrwXaT2ImxP7PyFZopKvN2YEs97xs0	2025-05-28 15:31:06.792165-04
j0g6d4ckdsngnloi5peztjpuwgfr2uck	.eJxVjMsOwiAQRf-FtSGU5-DSvd9AgBmkaiAp7cr479qkC93ec859sRC3tYZt0BJmZGdmHTv9jinmB7Wd4D22W-e5t3WZE98VftDBrx3peTncv4MaR_3W2Qvl0cqStTEAjqyxWnsNxRfKFJU2UijnJl1Q-ARyAkoFUACCiMay9wfxwjd2:1uFZOu:cpDQbuaA6bJapgKQBjDLusUI8p367xVv5P1CGPZAIfY	2025-05-29 10:17:32.013486-04
\.


--
-- Data for Name: workorders_workorder; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.workorders_workorder (id, job_description, estimated_cost, status, completed_at, created_at, updated_at, client_id) FROM stdin;
45	4 or 5 new pieces of art to hang @ 8 Great Oak. Any chance we can put Friday, May 23,	500.00	in_progress	\N	2025-04-27 07:07:27.405815-04	2025-04-27 07:07:27.413178-04	895
69	Pick up at Baboo and deliver and install at 4 Prentice Place Montauk \r\nBig ladder required	580.00	in_progress	\N	2025-05-02 22:27:58.595423-04	2025-05-02 22:27:58.609889-04	962
170	pick up a painting Artist:Gene Davis \r\nTitle: “Slip Horn”\r\nDimensions 71.5x95.5\r\nFrom: Sothebys LIC\r\nDelivery to:\r\n47 The Circle \r\nEast Hampton, NY\r\nRoderic@rsteinkamp.com	600.00	in_progress	\N	2025-05-11 18:24:18.220353-04	2025-05-11 18:24:18.229882-04	1061
40	Artworks:\r\nMay Stevens\r\nSometimes the sun the moon, 2005\r\nMixed media \r\nPacked @ 27 x 3 x 22 in H\r\n\r\nMay Stevens\r\nSkylight, 2006\r\nLithograph and silkscreen\r\nEdition 53 of 75\r\nPacked @ 35 x 3 x 27 in H\r\nDelivered and installed at\r\nLynn Freedman and David Frankel\r\n1190 Brick Kiln Road\r\nSag Harbor, NY 11963\r\nUNITED STATES\r\nCell  914.316.8590	480.00	completed	2025-04-24 21:57:44.951424-04	2025-04-24 21:55:24.107202-04	2025-04-24 21:57:44.951494-04	877
101	install 2 pieces of art at 303 Park Ave #1916 Waldorf Condo on May 21st.	280.00	in_progress	\N	2025-05-05 14:10:20.832101-04	2025-05-05 14:10:20.840082-04	992
43	collect larger paintings from Hunt Slonem’s studio in Manhattan sometime before June. inches (there is also a 44 x 77 inch).  There are about 10 large & med-size paintings. Maybe a few more smaller paintings will be thrown in too	\N	pending	\N	2025-04-25 21:18:51.53526-04	2025-04-25 21:18:51.540347-04	765
44	Installs at 8 Ogden Lane Quogue, NY	280.00	in_progress	\N	2025-04-26 13:26:07.159591-04	2025-04-26 13:26:07.16691-04	894
133	Screenshot 2025-04-15 at 1.59.59 PM.png\r\nHeather Day\r\nOpen Petal (Cobalt), 2024\r\nAcrylic on canvas\r\n56 x 72 inches\r\n*WILL ALREADY BE AT THE HOUSE\r\n\r\nScreenshot 2025-04-15 at 2.00.57 PM.png\r\nAlex Katz \r\nElizabeth, 2024\r\nArchival Pigment on Innova Etching Cotton Rag 315 gsm paper\r\n30 x 60 inches - unframed dimensions\r\n*NEEDS TO BE PICKED UP FROM CITY FRAME\r\n259 West 30th Street 5th Floor\r\nNew York, NY 10001\r\n\r\nDELIVERY & INSTALLATION ADDRESS: \r\n51 Mecox Bay Lane\r\nWater Mill NY 11976	560.00	in_progress	\N	2025-05-08 16:53:31.29442-04	2025-05-08 16:53:31.313181-04	1025
42	Morgan’s \r\n342 Town Line Road \r\nSagaponack on Thursday 5/8\r\nInstallations.	280.00	completed	2025-05-14 15:16:01.112763-04	2025-04-25 20:50:03.635851-04	2025-05-14 15:16:01.112831-04	507
167	Installs at 36 Rivers Road, East Hampton.	600.00	in_progress	\N	2025-05-09 12:23:35.864467-04	2025-05-09 12:23:35.88732-04	676
168	C A R V A L H O  P A R K \r\n\r\nCELL PHONE +1.231.590.5355  TELEPHONE +1.718.366.2550\r\nPick up framed painting soft packed 74" x 58" x 3"\r\n112 WATERBURY STREET, BROOKLYN, NY 11206\r\nMika's and Brad Finkelstein\r\n12 Fir Lane\r\nMontauk, NY\r\nMikal cell: 646-354-3084\r\nBrad cell: 917-328-8522	500.00	in_progress	\N	2025-05-09 14:42:03.676957-04	2025-05-09 15:09:55.506856-04	1059
172	Robin Aviv - Install	280.00	in_progress	\N	2025-05-12 17:10:38.629993-04	2025-05-12 17:10:38.738485-04	590
166	Deliver and install from SkyFrame to Henry St. Southampton	450.00	in_progress	\N	2025-05-09 08:07:45.864844-04	2025-05-14 14:44:41.952893-04	1058
173	1133 broadway suite 901\r\nInstalls	300.00	completed	2025-05-14 15:10:29.418646-04	2025-05-12 18:23:14.164519-04	2025-05-14 15:10:29.418721-04	1063
39	pick up and shadow box the five paintings \r\n3 paintings @ 72 x 84"\r\n2 paintings @ 49 x 59" on Tuesday 5/6 from Orient, NY and deliver them to Chelsea the following day for $960. \r\nfrom 385 oyster ponds lane, orient,NY11957	960.00	completed	2025-05-14 15:11:51.130095-04	2025-04-24 21:16:22.998574-04	2025-05-14 15:11:51.130164-04	853
67	hanging 3–4 mirrors in the house	280.00	completed	2025-05-14 15:23:43.146355-04	2025-04-30 21:06:14.756336-04	2025-05-14 15:23:43.146424-04	959
68	Pick up in City 415 East 52nd street #4CB (between 1st and the East River then deliver and install in Shelter Island.	1200.00	completed	2025-05-14 15:23:51.804872-04	2025-05-02 22:02:23.621739-04	2025-05-14 15:23:51.804943-04	961
41	Pick up at 87 Crosby St. and deliver to Southampton \r\nBobby Gerry \r\n68 x 48 x 3 to\r\n88 Hill Street \r\nAnd \r\n20 Breese Lane\r\nBeier.\r\n51 x 42 x 3\r\n42 x 63 x 3\r\n37 x 28 1/2 x3\r\n23 x 20 x 2\r\n26 x 33 x 3\r\n\r\nBobby Gerry \r\n68 x 48 x 3	580.00	completed	2025-05-14 15:14:52.122079-04	2025-04-25 20:39:51.266646-04	2025-05-14 15:14:52.12215-04	893
100	In\r\n15 Fairlea Ct\r\nSag Harbor, NY 11963-4311	500.00	completed	2025-05-14 15:26:06.666466-04	2025-05-03 15:40:10.43826-04	2025-05-14 15:26:06.666536-04	959
174	Installs at 28 Second Neck Lane, Quogue	700.00	in_progress	\N	2025-05-14 15:42:17.543576-04	2025-05-14 15:42:17.550171-04	1093
199	Hang one framed photo at 149 E. 73rd St., Apt. 10	280.00	in_progress	\N	2025-05-16 19:07:16.818366-04	2025-05-16 19:07:16.831575-04	1094
201	Installs at 101 West 67th St, NY 10023\r\nInto concrete.	500.00	in_progress	\N	2025-05-17 21:30:56.966186-04	2025-05-17 21:30:56.97361-04	1095
\.


--
-- Data for Name: invoices_invoice; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invoices_invoice (id, invoice_number, date_created, due_date, amount, status, notes, client_id, work_order_id) FROM stdin;
1	INV-20250514-4155	2025-05-14	2025-05-14	580.00	unpaid	Pick up at 87 Crosby St. and deliver to Southampton \r\nBobby Gerry \r\n68 x 48 x 3 to\r\n88 Hill Street \r\nAnd \r\n20 Breese Lane\r\nBeier.\r\n51 x 42 x 3\r\n42 x 63 x 3\r\n37 x 28 1/2 x3\r\n23 x 20 x 2\r\n26 x 33 x 3\r\n\r\nBobby Gerry \r\n68 x 48 x 3	893	\N
2	INV-20250514-8873	2025-05-14	2025-05-14	280.00	unpaid	Morgan’s \r\n342 Town Line Road \r\nSagaponack on Thursday 5/8\r\nInstallations.	507	\N
4	INV-20250514-8261	2025-05-14	2025-05-14	500.00	unpaid	Installing mirrors in the house	959	\N
\.


--
-- Data for Name: workorders_event; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.workorders_event (id, event_type, address, date, work_order_id) FROM stdin;
49	pickup	507 W. 24th Street New York, NY	2025-04-23	40
50	deliver_install	1190 Brick Kiln Road Sag Harbor, NY 11963	2025-04-24	40
47	pickup_wrap	385 oyster ponds lane, orient,NY11957	2025-05-06	39
48	dropoff	507 W. 24th Street New York, NY	2025-05-07	39
51	pickup	87 Crosby St. New York, NY	2025-05-07	41
52	dropoff	88 Hill St. Southampton, NY	2025-05-08	41
53	install	342 Town Line Rd. Sagaponack, NY	2025-05-08	42
54	install	8 Ogden Lane Quogue, NY	2025-04-28	44
55	install		2025-05-23	45
67	install		2025-05-09	67
68	pickup_wrap	415 east 52nd street 4CB	2025-05-05	68
69	pickup	Baboo	2025-05-05	69
70	deliver_install	4 Prentice Place Montauk, NY	2025-05-16	69
100	install	Sag Harbor	2025-05-09	100
101	install	303 Park Ave	2025-05-21	101
133	pickup	W. 30 City Frame	2025-05-21	133
134	deliver_install	51 Mecox Bay Lane	2025-05-23	133
135	pickup	SkyFrame	2025-05-14	166
136	deliver_install	Henry St Southampton	2025-05-15	166
137	install	36 Rivers Road,  East Hampton.	2025-05-15	167
138	pickup	112 WATERBURY STREET, BROOKLYN, NY	2025-05-13	168
139	deliver_install	Finkelstein 12 Fir Lane Montauk, NY	2025-05-20	168
142	pickup	Gantry Point Long Island City	2025-05-13	170
143	deliver_install	34 The Circle East Hampton	2025-05-20	170
146	install	30 Halsey Lane, Watermill	2025-05-20	172
147	install	1133 Broadway nyc	2025-05-13	173
148		15 Fairlea Ct, Sag Harbor, NY 11963	\N	67
149	install	28 Second Neck Lane, Quogue, NY	2025-05-22	174
150	install	149 E. 73rd St., Apt. 10	2025-05-21	199
152	install	101 West 67th St, NY 10023	2025-05-21	201
\.


--
-- Data for Name: workorders_jobattachment; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.workorders_jobattachment (id, file, uploaded_at, work_order_id) FROM stdin;
39		2025-04-24 21:16:23.017354-04	39
41	job_attachments/IMG_2337.jpeg	2025-04-24 21:55:24.124573-04	40
42		2025-04-24 21:58:24.77774-04	39
43		2025-04-24 22:02:36.0039-04	39
44		2025-04-25 19:52:08.410252-04	39
45		2025-04-25 20:39:51.278783-04	41
46		2025-04-25 20:50:03.646344-04	42
47		2025-04-25 21:18:51.543099-04	43
48		2025-04-26 13:26:07.170032-04	44
49		2025-04-27 07:07:27.415561-04	45
67		2025-04-30 21:06:14.78941-04	67
68		2025-05-02 22:02:23.631367-04	68
69		2025-05-02 22:27:58.612444-04	69
100		2025-05-03 15:40:10.484482-04	100
101		2025-05-05 14:10:20.842778-04	101
102		2025-05-05 14:17:56.159182-04	100
133		2025-05-08 16:53:31.318693-04	133
166		2025-05-09 08:07:45.896104-04	166
167		2025-05-09 12:23:35.894676-04	167
168		2025-05-09 14:42:03.738265-04	168
169		2025-05-09 15:09:55.50904-04	168
171		2025-05-11 18:24:18.232432-04	170
173		2025-05-12 17:10:38.748614-04	172
174		2025-05-12 18:23:14.17308-04	173
175		2025-05-14 14:44:41.959298-04	166
176		2025-05-14 15:12:44.082066-04	41
177		2025-05-14 15:13:44.484206-04	41
178		2025-05-14 15:15:29.241302-04	42
179		2025-05-14 15:21:56.831359-04	67
180		2025-05-14 15:23:10.81186-04	67
181		2025-05-14 15:25:36.789662-04	100
182		2025-05-14 15:42:17.552316-04	174
183		2025-05-16 19:07:16.835844-04	199
185		2025-05-17 21:30:56.975814-04	201
\.


--
-- Data for Name: workorders_jobnote; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.workorders_jobnote (id, note, created_at, work_order_id) FROM stdin;
39		2025-04-24 21:16:23.020106-04	39
41		2025-04-24 21:55:24.128502-04	40
42		2025-04-24 21:58:24.780676-04	39
43		2025-04-24 22:02:36.007448-04	39
44		2025-04-25 19:52:08.414615-04	39
45		2025-04-25 20:39:51.281714-04	41
46		2025-04-25 20:50:03.649578-04	42
47		2025-04-25 21:18:51.546321-04	43
48		2025-04-26 13:26:07.172536-04	44
49		2025-04-27 07:07:27.418357-04	45
67		2025-04-30 21:06:14.801038-04	67
68		2025-05-02 22:02:23.634423-04	68
69		2025-05-02 22:27:58.615045-04	69
100		2025-05-03 15:40:10.494395-04	100
101		2025-05-05 14:10:20.845609-04	101
102		2025-05-05 14:17:56.161962-04	100
133		2025-05-08 16:53:31.327875-04	133
166		2025-05-09 08:07:45.906358-04	166
167		2025-05-09 12:23:35.902171-04	167
168		2025-05-09 14:42:03.778257-04	168
169		2025-05-09 15:09:55.511599-04	168
171		2025-05-11 18:24:18.235201-04	170
173		2025-05-12 17:10:38.754502-04	172
174		2025-05-12 18:23:14.179174-04	173
175		2025-05-14 14:44:41.962017-04	166
176		2025-05-14 15:12:44.084844-04	41
177		2025-05-14 15:13:44.490341-04	41
178		2025-05-14 15:15:29.244464-04	42
179		2025-05-14 15:21:56.833789-04	67
180		2025-05-14 15:23:10.814583-04	67
181		2025-05-14 15:25:36.792858-04	100
182		2025-05-14 15:42:17.55492-04	174
183		2025-05-16 19:07:16.840152-04	199
185	10:30 a.m.	2025-05-17 21:30:56.978532-04	201
\.


--
-- Name: accounts_customuser_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.accounts_customuser_groups_id_seq', 1, false);


--
-- Name: accounts_customuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.accounts_customuser_id_seq', 132, true);


--
-- Name: accounts_customuser_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.accounts_customuser_user_permissions_id_seq', 212, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 33, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 66, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 66, true);


--
-- Name: clients_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.clients_client_id_seq', 1095, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 528, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 33, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 33, true);


--
-- Name: invoices_invoice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.invoices_invoice_id_seq', 4, true);


--
-- Name: workorders_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.workorders_event_id_seq', 152, true);


--
-- Name: workorders_jobattachment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.workorders_jobattachment_id_seq', 185, true);


--
-- Name: workorders_jobnote_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.workorders_jobnote_id_seq', 185, true);


--
-- Name: workorders_workorder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.workorders_workorder_id_seq', 201, true);


--
-- PostgreSQL database dump complete
--

