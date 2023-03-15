DROP TABLE IF EXISTS `UserTable`;

CREATE TABLE `UserTable` (
  `user_id` mediumint(8) unsigned NOT NULL auto_increment,
  `user_name` varchar(255) NOT NULL,
  `user_surname` varchar(255) NOT NULL,
  `user_email` varchar(255) NOT NULL,
  `user_pass` varchar(255) NOT NULL,
   `encrypted_data` varbinary(max),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

INSERT INTO `UserTable` (`user_name`,`user_surname`,`user_email`,`user_pass`)
VALUES
  ("Erasmus","Arnold","lacus@aol.net","AD2215657283042881814488"),
  ("Alvin","Wall","egestas.nunc.sed@google.com","FO4392218173247234"),
  ("Dana","Sims","velit.justo@google.net","LI6725741542523021878"),
  ("Conan","Kaufman","quam.pellentesque@hotmail.ca","CH5058851507322511529"),
  ("Kiara","Roach","accumsan.convallis.ante@icloud.net","SK3197534754067903074332"),
  ("Erasmus","Black","consectetuer.adipiscing@aol.org","HR3481959993417135258"),
  ("Imogene","Rocha","quis.pede@icloud.couk","PT81905661374604881321218"),
  ("Kim","Clayton","enim@outlook.net","FI7543355314328946"),
  ("Moses","Acevedo","in.aliquet@outlook.edu","FR9580452537683581898771431"),
  ("Jordan","Ward","luctus.ut.pellentesque@google.ca","MC7883659950011445449517461");
INSERT INTO `UserTable` (`user_name`,`user_surname`,`user_email`,`user_pass`)
VALUES
  ("Cleo","Rivers","elit.aliquam.auctor@yahoo.org","GT10858640478935032793817174"),
  ("Evangeline","Shepherd","phasellus.ornare@aol.couk","MD7136597846388257747717"),
  ("Edward","Grant","integer@protonmail.org","RS27397451757755238266"),
  ("Melyssa","Hendricks","cursus@icloud.net","GI22JDYF946512583749465"),
  ("Cruz","Logan","non.massa@hotmail.net","TR621389213531470776189975"),
  ("Stacey","Maxwell","urna.vivamus@icloud.edu","MU0455181883228578068997467547"),
  ("Bernard","Rosario","dolor@protonmail.couk","LU421711771522504217"),
  ("Daria","Cruz","et@protonmail.com","MT77PETV90711304622368521982136"),
  ("Rajah","Lee","interdum.sed@icloud.ca","SA1932040149116521924888"),
  ("Minerva","Hunt","posuere.vulputate@google.couk","HR3676237641346116562");
INSERT INTO `UserTable` (`user_name`,`user_surname`,`user_email`,`user_pass`)
VALUES
  ("Lillith","Mclaughlin","vulputate.eu@yahoo.com","AZ59348569743822116952142489"),
  ("Chaim","Knapp","magna.ut.tincidunt@icloud.ca","PT24053814747343428391411"),
  ("Eugenia","Brewer","justo.eu@protonmail.org","SM3738881432644213108427663"),
  ("Patrick","Lucas","laoreet@hotmail.net","GR8967484317884881757781855"),
  ("Lewis","Dillard","ante.blandit@icloud.net","DO77053633871318727126535467"),
  ("Felicia","Garner","sem.mollis.dui@protonmail.com","MK56119393407856465"),
  ("Alexandra","Horne","vulputate.velit@protonmail.ca","MD8468391137112299825347"),
  ("Tatum","Davenport","vel.lectus.cum@hotmail.org","DO67407904558326141612384078"),
  ("Maxwell","Acevedo","nunc@protonmail.com","MR6483272687273981424929553"),
  ("Emmanuel","Thomas","sagittis.felis.donec@google.com","IS434475399000772644313860");
INSERT INTO `UserTable` (`user_name`,`user_surname`,`user_email`,`user_pass`)
VALUES
  ("Adria","Navarro","enim@google.ca","LI4816658728617642884"),
  ("Meghan","Foley","orci.donec@yahoo.org","ES8222281698647656292676"),
  ("Edan","Stein","sed.tortor.integer@hotmail.org","PL32265742053638514441196260"),
  ("Zorita","Roman","mus.donec@protonmail.edu","BH05181762615367731860"),
  ("Wyoming","Walters","nunc.quisque@yahoo.org","GE26083196851781789738"),
  ("Nathaniel","Williams","taciti.sociosqu@aol.net","IS351878325143776147595534"),
  ("Dolan","Mayo","luctus@protonmail.org","CH6086132828212542557"),
  ("Stella","Barlow","lorem@hotmail.org","FI9256620643823712"),
  ("James","Brennan","mauris.nulla.integer@aol.edu","BG53GDJY52557378625274"),
  ("Willow","Thomas","proin@google.org","DE26465667221138963835");
INSERT INTO `UserTable` (`user_name`,`user_surname`,`user_email`,`user_pass`)
VALUES
  ("Mallory","Diaz","quis.pede@google.com","BH90823327241439845415"),
  ("Elizabeth","Gill","non.enim@google.net","DK2340866746996603"),
  ("Azalia","Hogan","nisl.elementum@icloud.com","PK2975687878265610387722"),
  ("Shellie","Patel","diam.proin@protonmail.org","BE10321956126347"),
  ("Venus","Dalton","magna.suspendisse.tristique@icloud.edu","VG7716664748018245168627"),
  ("Brennan","Mcfadden","sed.dui.fusce@hotmail.com","DO40521267672637522861577155"),
  ("Alexis","Cummings","eu.tellus.phasellus@yahoo.couk","LT918257672735837378"),
  ("Burton","Howard","ultrices@icloud.net","GE81808518458838881147"),
  ("Elijah","Randall","scelerisque.dui.suspendisse@aol.net","SE6293259859373685536162"),
  ("Raya","Wiley","enim.etiam@yahoo.edu","LI8072020736328944320");
INSERT INTO `UserTable` (`user_name`,`user_surname`,`user_email`,`user_pass`)
VALUES
  ("Solomon","Gay","a.neque@protonmail.edu","SE5070077818223586081332"),
  ("Carson","Gregory","vestibulum.nec@aol.com","PS691543899243962197174327552"),
  ("Hashim","Albert","egestas@hotmail.couk","MC1343898371617684238560723"),
  ("Kylan","Ball","amet.consectetuer@google.ca","SM6753526459364459203877491"),
  ("Chaney","Workman","donec.consectetuer@aol.couk","PS452879188377428453324358979"),
  ("Rina","Fisher","per.conubia@google.ca","GE46744565228812452583"),
  ("Thane","Wolfe","a.malesuada.id@yahoo.couk","SK2476248872530547273495"),
  ("Nicole","Vance","augue.ac.ipsum@outlook.org","FR2137201454868367190652593"),
  ("Mercedes","Kidd","semper.egestas@google.ca","TR492278692568838675996973"),
  ("Armand","Velazquez","orci.phasellus.dapibus@icloud.couk","DK5093665874207653");
INSERT INTO `UserTable` (`user_name`,`user_surname`,`user_email`,`user_pass`)
VALUES
  ("Rashad","Jimenez","nulla.dignissim@google.net","LV90XKWN7402197186122"),
  ("Kevin","Newton","scelerisque.mollis@icloud.com","DE58448194058775831778"),
  ("Uta","Moreno","orci.ut.semper@aol.ca","ME65621940628177633465"),
  ("Erasmus","Burke","consectetuer.euismod@aol.edu","KW1271149807619637202477726430"),
  ("Cathleen","Ellis","dui.suspendisse.ac@hotmail.org","PT55264715762767533733336"),
  ("Rigel","Diaz","pellentesque.habitant@google.ca","BE53669683401345"),
  ("Velma","Cantrell","interdum@hotmail.net","IT275HQRKI50151741660814830"),
  ("Jordan","Douglas","tellus.imperdiet@google.org","GB14REPP73106252356476"),
  ("Lee","Odom","pede.et@google.couk","MC5162521312498229978535220"),
  ("Tanner","Hicks","dignissim.magna@aol.org","DE68667728598327753277");
INSERT INTO `UserTable` (`user_name`,`user_surname`,`user_email`,`user_pass`)
VALUES
  ("Reese","Richardson","eu@hotmail.com","NO1914596774262"),
  ("Piper","Callahan","a.malesuada@icloud.edu","DE54447354505880155186"),
  ("Joel","Villarreal","ut@protonmail.edu","SI29943490417143377"),
  ("Kyra","Petersen","quisque.ac.libero@yahoo.edu","AZ61550491807318968693747337"),
  ("Nerea","Boyle","mauris.suspendisse@aol.edu","MD1645124654315363218430"),
  ("Paula","Hopkins","dignissim.maecenas.ornare@protonmail.com","SA7940975670034079654935"),
  ("Tate","Valencia","ligula.nullam.feugiat@google.edu","IL661211419959617577685"),
  ("Daquan","Foreman","nunc.risus@google.edu","DE05433815415727563274"),
  ("Elliott","Gilbert","dictum.eu.placerat@aol.org","BH09533262132377385687"),
  ("Marvin","Merritt","proin.non@hotmail.com","AZ95281580297338588496981474");
INSERT INTO `UserTable` (`user_name`,`user_surname`,`user_email`,`user_pass`)
VALUES
  ("Avram","Brady","lorem.donec@protonmail.net","FO4080834021771532"),
  ("TaShya","Holt","dolor@google.net","GR0570142538655769388779264"),
  ("Wynter","Hutchinson","ipsum.suspendisse@yahoo.com","CY08328266178452128837642800"),
  ("Anjolie","Ortega","dictum@yahoo.couk","CZ2454515786866855121255"),
  ("Jeremy","Jensen","augue@icloud.com","TR856594368331006579977486"),
  ("Elijah","English","suspendisse.dui@yahoo.edu","MT55AGVJ81321053693884351461036"),
  ("Guy","Simmons","lorem@hotmail.com","BE33715580886467"),
  ("Mari","Dyer","ultrices.posuere@aol.ca","AL82758807897080107957423632"),
  ("Lars","Garner","fermentum.vel@icloud.edu","KW1295644152126886533461276734"),
  ("Ima","Rosa","ac.ipsum@hotmail.couk","HU40132619441238015423716253");
INSERT INTO `UserTable` (`user_name`,`user_surname`,`user_email`,`user_pass`)
VALUES
  ("Chester","Lowe","ipsum.dolor.sit@icloud.net","AZ85047250545610078822010837"),
  ("Winifred","Franco","venenatis@outlook.ca","VG1411444547344054076462"),
  ("Barclay","Velazquez","justo@icloud.com","FR2067442622176801207397405"),
  ("Zeph","Flowers","non.nisi@protonmail.net","MU6102373051631623042545518628"),
  ("Magee","Mckay","a.aliquet@icloud.edu","AD6351192614870436862125"),
  ("Kadeem","Underwood","mi.aliquam@icloud.couk","IL924748320647262212238"),
  ("Macaulay","Brock","tellus.justo.sit@hotmail.edu","CZ4731841848067489817383"),
  ("Ryan","Juarez","tincidunt@icloud.net","ME11345492358695577636"),
  ("Abraham","Hahn","sed@hotmail.org","SM3920895262552911373813346"),
  ("Miriam","Bond","velit.eu.sem@icloud.com","DE29578532290627455488");


CREATE SYMMETRIC KEY encryption_key
WITH ALGORITHM = AES_256
ENCRYPTION BY user_passWORD = 'Youruser_password';

UPDATE UserTable
SET encrypted_data = ENCRYPTBYKEY(KEY_GUID('encryption_key'), user_pass);

SELECT CONVERT(varchar(max), DECRYPTBYKEY(encrypted_data)) AS user_pass
FROM UserTable;
