# **Az AntiGravity Runtime architektúrája: Állapot-horgonyzás, procedurális memória és kormányzási protokollok az ágensi szoftverfejlesztésben**

Az ágens-központú fejlesztési paradigmák megjelenése alapvetően formálja át a modern szoftverfejlesztési életciklust, ahol az artificial intelligence (AI) már nem csupán kiegészítő eszközként, hanem autonóm munkafolyamat-architektúraként jelenik meg. A Google AntiGravity platformja ezen evolúció élvonalát képviseli, egy olyan integrált környezetet biztosítva, ahol a Gemini 3 alapú ágensek képesek a tervezésre, a kódolásra és az autonóm ellenőrzésre. Ez a jelentés részletesen elemzi az AntiGravity runtime belső működését, különös tekintettel az állapot-horgonyzás (State Anchor), a procedurális memória szintézise és a 00-09 szintű kormányzási rétegek (Governance layers) közötti szinergiákra. Az elemzés rávilágít arra, hogy a determinisztikus kimenetek elérése érdekében miként váltja fel a probabilisztikus következtetést a strukturált, kódalapú emlékezet és a szigorú képesség-promoválási kapuk rendszere.

## **Az ágens-első IDE architektúra és a menedzser-felület evolúciója**

A hagyományos integrált fejlesztői környezetek (IDE) az AI-t jellemzően "copilot" üzemmódban integrálták, ahol az algoritmusok csupán kiegészítették a fejlesztő munkáját. Ezzel szemben az AntiGravity egy ágens-első (agent-first) környezet, amelyben a felületek — a szerkesztő, a terminál és a böngésző — magába az ágensbe vannak beágyazva.1 Ez a megközelítés lehetővé teszi, hogy az ágensek párhuzamosan és aszinkron módon operáljanak több felületen, miközben a fejlesztő stratégiai orkesztrátorként felügyeli a folyamatokat.2

A platform központi eleme a menedzser-felület (Manager surface), amely "Mission Control" központként funkcionál. Itt történik a specializált ágensek létrehozása, koordinálása és megfigyelése.1 Az AntiGravity ágensei nem csupán kódsorokat sugallnak, hanem "artefaktumokat" hoznak létre — olyan eredménytermékeket, mint a végrehajtási tervek, böngésző-felvételek és feladatlisták, amelyek megkönnyítik az emberi ellenőrzést a nyers eszközhívásokkal szemben.1

### **A vezető AI-natív fejlesztői környezetek összehasonlító elemzése**

| Jellemző | Cursor | Windsurf | Google AntiGravity |
| :---- | :---- | :---- | :---- |
| **Alaparchitektúra** | VS Code Fork | VS Code Fork | VS Code Fork 3 |
| **Interakciós paradigma** | Chat / Soron belüli | Flow / Ágens panel | Manager Surface (Orkesztráció) 1 |
| **Modellválaszték** | Multi-modell | Multi-modell | Gemini 3, Claude, GPT-OSS 1 |
| **Verifikációs mechanizmus** | Manuális review | Terminál logok | Artefaktum-alapú (Böngésző/Terv) 1 |
| **Memóriakezelés** | Munkamenet-alapú | Munkamenet-alapú | Állapot-horgonyzás & Tudásbázis 4 |
| **Kormányzási modell** | Helyi szabályok | Helyi szabályok | 00-09 Kormányzási rétegek 6 |

Az AntiGravity rugalmasságát növeli, hogy a fejlesztők nem korlátozódnak a Google modelljeire; választhatnak az Anthropic Claude Sonnet 4.5 vagy az OpenAI nyílt súlyú GPT-OSS modelljei közül is.1 Ez a többmodelles megközelítés lehetővé teszi a feladat-specifikus optimalizálást, ahol a Gemini 3 Pro a nagy kontextusablakot igénylő refaktorálási feladatokat, míg más modellek a specifikus logikai ellenőrzéseket végezhetik.1

## **Állapot-horgonyzás és a Megértés és Kontextus jelentősége**

Az autonóm ágensek egyik legnagyobb kihívása a hosszú távú munkamenetek során fellépő kontextus-összeomlás vagy "amnézia", ahol az ágens elveszíti a fókuszt a célkitűzés felett a növekvő beszélgetési előzmények miatt.8 Az AntiGravity ezt a problémát az állapot-horgonyzás (State Anchor) technológiájával oldja meg, amely a magyar fejlesztői közösségben "Megértés és Kontextus" néven vált ismertté.9 Ez a mechanizmus biztosítja, hogy az ágens aktuális állapota és céljai függetlenek maradjanak a token-kiszorulástól vagy a kontextusablak korlátaitól.5

### **A lineáris állapot-horgonyzás mechanikája**

A lineáris állapot-horgonyzás egy külső program-számlálóként (Program Counter) funkcionál az ágens számára. A todos eszköz segítségével az ágens egy strukturált objektumba szerializálja az implementációs tervét, amely a kontextusablak tetején marad rögzítve.5 Ez megakadályozza a kontextus-eltolódást (context drift), ami akkor következik be, ha a modell minden egyes fordulóban újraértelmezi a teljes előzményt, és fokozatosan eltér az eredeti szándéktól.8

A kutatások azt mutatják, hogy a hagyományos architektúrákban a hosszú munkamenetek körülbelül ![][image1]\-a végződik amnéziával, míg az állapot-horgonyzás ezt az arányt ![][image2] alá csökkenti.8 Ez az eredmény azáltal érhető el, hogy a kritikus logikát a probabilisztikus promptból determinisztikus kódstruktúrákba helyezik át, amelyek "kemény korlátként" (hard rails) szolgálnak az ágens következtetési folyamataihoz.8

### **Az állapot-horgonyzás technikai összetevői és hatásai**

| Összetevő | Funkció | Implementációs részlet |
| :---- | :---- | :---- |
| **State Anchor** | Az igazság változhatatlan rekordja | Minden kontextus-forduló elején injektálva 5 |
| **todos eszköz** | Külső program-számláló | A tervet egy todos objektumba szerializálja 11 |
| **Rollback triggerek** | Konfliktuskezelés | Visszaáll az utolsó jó állapotra, ha ellentmondást észlel 8 |
| **Státusz-követés** | Kényszerítő funkció | pending, in\_progress és completed címkék 5 |

A magyar kontextusban a "Megértés és Kontextus" fogalma mélyebb szemantikai alapozást igényel. A fejlesztők tapasztalata szerint a tiszta kódbázisok és a jól definiált üzleti igények átadása elengedhetetlen ahhoz, hogy az ágens ne csupán "vibe-alapú" kódolást végezzen, hanem valóban értse a szoftverarchitektúra összefüggéseit.10 Az állapot-horgonyok immutábilis rekordokként való kezelése biztosítja, hogy ha egy epizód ellentmond a korábbi döntéseknek, a rendszer azonnal elutasítsa a kimenetet és kényszerítse a modell explicit állapot-frissítését.8

## **Procedurális memória szintézise és a tudományos módszertan**

Az AntiGravity platform a procedurális memória irányába mutat, ahol az ágens képességeit nem természetes nyelvű utasítások, hanem végrehajtható, determinisztikus kód formájában reprezentálják.5 Ezen emlékezet szintézise egy szigorú "tudományos módszertant" követ, amely több fázison keresztül finomítja az ágens képességeit a prototípustól a produkciós szintű készségig.11

### **A Hipotézis, Próba és Kód (Hypothesize, Probe, Code) keretrendszer**

A procedurális memória kialakítása során az ágensnek négy kritikus hiányosságot (gap) kell áthidalnia:

1. **Felfedezési hiány (Discovery Gap)**: Az ágensnek navigálnia kell a hatalmas eszköz-regiszterekben (például Model Context Protocol szerverek) anélkül, hogy túlterhelné a kontextusablakot több ezer JSON sémával.5 Ezt a dinamikus többszörös hívási protokoll (Dynamic MCP) kezeli, amely csak a szükséges sémákat tölti be "just-in-time" módon, fenntartva az ![][image3] kontextus-költséget.12  
2. **Verifikációs hiány (Verification Gap)**: A logika megírása előtt az ágensnek el kell végeznie egy "próba fázist" (Probe Phase). Ez magában foglalja az API hívását minimális limitekkel és a nyers adatstruktúra ellenőrzését (Stdout Grounding), hogy elkerülje a sémák hallucinálását.11  
3. **Dekompozíciós hiány (Decomposition Gap)**: A lineáris állapot-horgonyzás segítségével az ágens atomi lépésekre bontja a feladatot. Ez lehetővé teszi a modularitást és a verifikációs mérföldkövek beiktatását a tömeges műveletek előtt.5  
4. **Skálázási hiány (Scaling Gap)**: A prototípus kódot produkcióképessé teszi az aszinkron konkurens futtatás (például asyncio), az idempotencia-őrök és a külső perzisztencia mechanizmusok bevezetésével, amelyek megakadályozzák a duplikált feldolgozást rendszerösszeomlás után.11

A procedurális memória nem csupán a kód újrajátszásáról szól; ez a folyamat magában foglalja a készségek "megkeményítését" (hardening), ahol a validált logika egy verziózott kódbankba kerül.12 Az adatok azt mutatják, hogy a CodeMEM keretrendszert használó rendszerek — mint például a Gemini 3 — ![][image4]\-os helyességet érnek el az összetett munkafolyamatokban.12 Ez a determinisztikus architektúra garantálja, hogy ugyanazon bemenet és tárolt logika esetén az ágens mindig ugyanazt a kimenetet produkálja, kiküszöbölve az LLM-ekre jellemző sztochasztikus mintavételezést.12

## **Kormányzási rétegek (00-09) és szabály-hierarchia**

Az AntiGravity ökoszisztémát egy többszintű kormányzási rétegrendszer szabályozza, amely biztosítja, hogy az ágens viselkedése összhangban maradjon a szervezeti előírásokkal, a biztonsági protokollokkal és a technikai preferenciákkal. Ez a 00-09-es skála a szabályok fokozatos felfedésén és kényszerítésén alapul.6

### **A szabály-hierarchia és a megfelelőségi rétegek**

| Rétegtartomány | Kategória | Felügyelet és hatókör |
| :---- | :---- | :---- |
| **L0-L2** | **Rendszerszintű szabályok** | Immutábilis direktívák a Google DeepMind-tól; az ágens identitását és alapvető biztonságát definiálják.6 |
| **L3-L6** | **Globális szabályok** | Felhasználó által definiált preferenciák, amelyek minden projektre érvényesek (például "Mindig használj TypeScript-et").6 |
| **L7-L9** | **Munkaterületi szabályok** | Projekt-specifikus szabványok, amelyeket .cursorrules vagy .agent/rules fájlokban rögzítenek.6 |

Ez a struktúra megakadályozza a "kontextus-robbanást" (Context Explosion) azáltal, hogy csak a logikailag releváns rétegeket tölti be az ágens aktuális gondolkodási terébe.15 A "fokozatos felfedés" (Progressive Disclosure) architektúra biztosítja, hogy a magas szintű metaadatok (Level 1\) mindig be legyenek töltve, míg a teljes utasításkészletek (Level 2\) és a súlyos erőforrások (Level 3\) csak akkor kerülnek a fájlrendszerről a kontextusba, ha a feladat specifikusan illeszkedik a készség leírásához.6

A biztonsági auditálás során minden készséget úgy kezelnek, mint egy telepítendő szoftvert. A SKILL.md fájlok ellenőrzése során vizsgálni kell, hogy a készség nem próbál-e hozzáférni érzékeny fájlokhoz (például .env vagy .ssh), és a mellékelt szkripteket manuálisan kell felülvizsgálni a hálózati hívások szempontjából.6 Az AntiGravity vállalati szintű megfelelőséggel indult, beleértve a SOC 2, ISO 27001 és FedRAMP tanúsítványokat, valamint a munkaterületi izolációt, ahol a böngésző-automatizálás egy külön Chrome profilban fut az adatbiztonság garantálása érdekében.6

## **Field Agent készségminták és moduláris tudásegységek**

A "Field Agent" készségkészletek olyan moduláris, szabványosított tudásegységek, amelyek kiterjesztik az AI asszisztensek képességeit. Ezek a készségek Markdown formátumban (SKILL.md) vannak tárolva, lehetővé téve, hogy a csapatok ne csak a kódot, hanem az ágens adott kódhoz való viszonyulásának "tudását" is megosszák a verziókezelő rendszerekben.6

### **A Field Agent készségkészletek auditálása és kritikája**

A frissen létrehozott Field Agent minták három fő területet fednek le, amelyek mindegyike specifikus munkafolyamatokat és ellenőrzési pontokat tartalmaz 1:

1. **Diagnostic Integrity (Biztonság)**: Ez a készség a munkaterület integritásának fenntartásáért felelős. A triggerek minden új loop\_id kezdetekor aktiválódnak. Az elemzés rávilágít, hogy a "State/stable.json" konkrét fájlra való hivatkozást pontosítani kell a kanonikus L1 fájlformátumok meghatározásával, hogy elkerülhetőek legyenek a téves pozitív riasztások.1  
2. **KB Harmonization (Kormányzás)**: A tudásbázisok szinkronizálását végzi a "Scan → Propose → Sync → Execute" munkafolyamaton keresztül. Kritikus észrevétel, hogy a generált könyvtárakat (például STREAMS/ vagy ARCHIVE/) ki kell zárni a vizsgálatból, hogy az automatikus refaktorálás ne fusson bele generált fájlokba, és meg kell határozni a "tiltott transzformációk" listáját a parancsvédelmi tokenek megőrzése érdekében.1  
3. **Federated Handshake (Több-repo)**: A több adattár közötti adatcserét és a szivárgásmentességet kezeli. A képesség alapértelmezés szerint a "VERIFY" elvet követi, de szüksége van egy rögzített "tükör sémára" (mirror schema), amely meghatározza a satellite\_id, state\_hash és a captured\_utc mezőket a géppel feldolgozható regisztrációs bejegyzésekhez.1

### **A Field Agent tudásegységek kategóriái és statisztikái**

| Domain | Egységek száma | Stratégiai fókusz |
| :---- | :---- | :---- |
| **Teljesítmény & Optimalizálás** | 50+ egység | Bundle méret, re-render optimalizálás 15 |
| **Fejlesztői keretrendszerek** | 100+ készség | Next.js, Python, React, Rust 15 |
| **Architektúra & Design** | 66 minta | Tervezési minták és rendszerszervezés 15 |
| **DevOps & Eszközök** | 40+ egység | CI/CD, SQL, Git automatizálás 15 |
| **AI & Ágens-fejlesztés** | 180+ szabály | MCP integrációk és ágens-logika 15 |

A készségek univerzális hordozhatóságát a Markdown szabvány biztosítja, így azok nemcsak az AntiGravity-ben, hanem a Claude Code, Cursor vagy Windsurf rendszerekben is alkalmazhatóak.15 A háromszintű betöltési architektúra — Metaadat, Utasítások és Erőforrások — biztosítja a hatékonyságot: a nehéz eszközök vagy szkriptek a fájlrendszeren maradnak, és csak a kimenetük kerül be az ágens kontextusába.6

## **FACT promoválás és képesség-kapuk**

A képességek "FACT" szintre való emelése az a folyamat, ahol egy ágens-készség a probabilisztikus prototípus fázisból a determinisztikus, produkciókész állapotba kerül.1 Ez a promoválási gate biztosítja, hogy csak alaposan tesztelt és verifikált logikák váljanak a procedurális memória részévé.12

### **A FACT promoválás feltételei és bizonyítékai**

A FACT státusz eléréséhez az AntiGravity keretrendszer explicit végrehajtási evidenciát követel meg. Ez magában foglalja a "füstteszt" (smoke test) jelentéseket, amelyek igazolják, hogy a készség hívása során a várt artefaktumok jöttek létre.1 A promoválási sablon az alábbi kötelező elemeket tartalmazza:

* **Test Execution Evidence (MUST)**: Konkrét naplók és artefaktumok a sikeres futtatásról.  
* **Rollback Stratégia**: Definíció arra az esetre, ha a készség hibát okozna a produkciós környezetben.  
* **Kockázati elemzés**: A készség által érintett attack surface és a lehetséges drift azonosítása.  
* **Peer Review**: Annak biztosítása, hogy a készség szerzője és az ellenőr ne ugyanaz a személy legyen, csökkentve az önmegerősítő audit hibákat.1

Ez a módszertan a "human-in-the-loop" tudományos fegyelmet erősíti, ahol a fejlesztő döntési kapuknál hagyja jóvá az ágens előléptetését. Amíg egy készség nem kapja meg a FACT minősítést, addig csak szimulált vagy kísérleti környezetben használható, és minden hívása fokozott verifikációt igényel.1

## **Federáció és többrétegű ágens-orkesztráció**

A modern vállalati környezetekben a feladatok gyakran több szolgáltatást és adattárat érintenek, ami szükségessé teszi az ágensek közötti koordinációt és a "Federated Handshake" protokoll alkalmazását.5 Az AntiGravity támogatja a többszörös ágens-párhuzamos végrehajtást, ahol különböző specializált egységek dolgoznak a feladat részterületein.21

### **A többszörös ágens-rendszerek (MAS) dinamikája**

Az AntiGravity menedzser-felülete lehetővé teszi több ágens egyidejű elindítását, ahol például egy ágens a refaktorálásért, egy másik az egységtesztek generálásáért, a harmadik pedig a dokumentációért felel.1 Ezek az ágensek egy közös memória-tárolón keresztül kommunikálnak, amely megosztja az egyéni tudást és az aktuális állapot-horgonyokat.23

A federált munkafolyamat során az ágensnek:

1. **Szemantikai keresést** kell végeznie az elérhető eszközök között.  
2. **Hándshike protokollon** keresztül igazolnia kell a hozzáférési jogosultságokat.  
3. **Adatszivárgás-ellenőrzést** kell végeznie a külső szolgáltatások (például Outlook vagy OneDrive) közötti adattranszfer során.1

A Model Context Protocol (MCP) ebben a folyamatban úgy működik, mint egy USB-C kábel: szabványosított kommunikációt tesz lehetővé az AI alkalmazások és a külső szolgáltatások között, kiküszöbölve a manuális kontextusváltásokat.22 Az MCP segítségével az ágens közvetlenül írhat SQL lekérdezéseket a Postgres adatbázisba vagy kezelhet jegyeket a GitHubon, miközben a biztonsági korlátok (például az izolált Chrome profilok) érvényben maradnak.6

## **Erőforrás-kezelés és technikai szűk keresztmetszetek**

Az AntiGravity runtime elemzése során feltárt technikai adatok rávilágítanak a platform erőforrás-igényére és a hardver-specifikus korlátokra. Bár a rendszer nagy hatékonysággal kezeli a logikai feladatokat, a memóriakezelés terén jelentős anomáliák figyelhetőek meg.24

### **Memóriahasználati anomáliák és virtualizációs hatások**

Az AntiGravity folyamatok extrém virtuális memória (VSZ) felfúvódást mutatnak. A fő folyamatok gyakran körülbelül ![][image5] virtuális címtartományt foglalnak le, miközben a tényleges fizikai RAM-használatuk (RSS) mindössze ![][image6].24 Ez a ![][image7] arányú különbség rávilágít az alábbi technikai okokra:

* **V8 Engine címtartomány-foglalása**: A JavaScript motor hatalmas területeket foglal le előre a heap és a JIT fordítási artefaktumok számára.24  
* **Electron/Chromium homokozó architektúra**: Minden egyes ágensfolyamat saját címtartományt tart fenn a folyamat-izoláció érdekében, ami ágensenként körülbelül 17-20 folyamatot jelent.24  
* **Memória-leképezett fájlok**: Az alkalmazás-csomagok többszörös leképezése a virtuális memóriába, ami növeli a kernel memóriakezelési terhelését.24

### **Hardver-kompatibilitási és bináris szintű kihívások**

A platform binárisai (például a language\_server\_linux\_arm) gyakran olyan modern ARM funkciókkal vannak fordítva (ARMv8.1+ instrukciók, LSE atomics, NEON optimalizációk), amelyek nem kompatibilisek a régebbi hardverekkel. Például a Raspberry Pi 4 Cortex-A72 processzora csak az alap ARMv8.0-A instrukciókat támogatja, ami SIGILL (Illegal Instruction) hibát és a szerver összeomlását okozza.25

| Metrika | Elvárt / Normál | AntiGravity Runtime |
| :---- | :---- | :---- |
| **VSZ folyamatonként** | **![][image8]** | **![][image5]** 24 |
| **RSS folyamatonként** | **![][image9]** | **![][image10]** 24 |
| **Swap használat** | Minimális | ![][image11] (3 példány esetén) 24 |
| **Folyamatok száma** | **![][image12]** | **![][image13]** ágensenként 24 |

A felhasználóknak javasolt a GPU gyorsítás letiltása (--disable-gpu) és a V8 heap limit manuális beállítása a memórianyomás csökkentése érdekében.15

## **Az ágens-alapú gazdaság és a jövőbeli kilátások**

Az AntiGravity nem csupán egy fejlesztői eszköz, hanem az "Ágens-alapú Gazdaság" (Agentic GDP) alapköve. 2026 elejére az autonóm módon működő láncon belüli ágensek aktivitási szintje először haladta meg az emberi felhasználókét, ahol az ágens-ágens (A2A) közötti arbitrázs és tárgyalás vált meghatározóvá.26

### **Az artefaktumok mint az auditálhatóság garanciái**

Ebben az új korszakban az artefaktum-rendszer válik a bizalom alapjává. Az ágensek által generált videofelvételek, implementációs tervek és feladatlisták lehetővé teszik a felhasználók számára, hogy ne vakon bízzanak a kódban, hanem vizuálisan és strukturáltan ellenőrizzék az ágens munkáját.1 Az artefaktumok közvetlenül kommentálhatóak (Google Docs stílusban), ami azonnali visszacsatolást és irányítást tesz lehetővé a fejlesztő számára.1

A jövőbeli fejlesztések iránya az öntanuló ágensek felé mutat, amelyek perzisztens tudásbázist tartanak fenn a korábbi munkáikról, emlékeznek a felhasználó építészeti preferenciáira és képesek az önevaluációra.1 Ez a folyamatos tanulási ciklus (Perceive → Reason → Act → Learn) biztosítja, hogy az ágensek idővel egyre hatékonyabbá és kontextus-tudatosabbá váljanak.27

## **Stratégiai következtetések és ajánlások**

Az AntiGravity runtime architektúrájának és a Field Agent készségkészleteknek a részletes elemzése alapján az alábbi stratégiai megállapítások tehetőek:

1. **Determinizmus kényszerítése**: Az állapot-horgonyzás nem csupán egy technikai funkció, hanem a megbízhatóság alapfeltétele. A fejlesztőknek törekedniük kell a "lineáris állapot-horgonyzás" alkalmazására minden összetett munkafolyamatban, hogy elkerüljék a kontextus-összeomlást.  
2. **Kormányzási fegyelem**: A 00-09-es rétegek szigorú betartása elengedhetetlen a biztonság és a technikai stílus fenntartásához. A készségek promoválása során a FACT kapu használata kötelező, amelyhez explicit futtatási bizonyítékokat kell csatolni.  
3. **Készség-modularitás**: A Field Agent készségeket (Diagnostic Integrity, KB Harmonization, Federated Handshake) folyamatosan frissíteni kell a tükör sémákkal és tiltott transzformációs listákkal, hogy minimalizálják az automatizált refaktorálás kockázatait.  
4. **Erőforrás-optimalizáció**: A VSZ bloat és a hardver-kompatibilitási kérdések miatt a vállalatoknak javasolt a fejlesztői gépek profilozása és a készségek futtatása előtt a "Probe Phase" alkalmazása a szoftver- és hardverigények pontos felméréséhez.

Az AntiGravity platform sikere abban rejlik, hogy képes áthidalni a szakadékot a probabilisztikus AI modellek és a determinisztikus mérnöki követelmények között. A procedurális memória és az artefaktum-alapú verifikáció egy olyan jövő felé mutat, ahol a fejlesztők nem csupán kódolók, hanem autonóm ágens-ökoszisztémák építészei és felügyelői.2 Az AntiGravity segítségével a szoftverfejlesztés egy mérhető, auditálható és skálázható folyamattá válik, amelyben a tudás nemcsak a fejekben, hanem verziózott, végrehajtható készségek formájában is létezik.

#### **Idézett munkák**

1. Antigravity Is Google's New Agentic Development Platform \- The ..., hozzáférés dátuma: március 1, 2026, [https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/)  
2. Online Google Antigravity Training \- Nobleprog Kuwait, hozzáférés dátuma: március 1, 2026, [https://www.nobleprog-kw.com/google-antigravity/training/online](https://www.nobleprog-kw.com/google-antigravity/training/online)  
3. What a Difference a VS Code Fork Makes: Antigravity, Cursor and Windsurf Compared, hozzáférés dátuma: március 1, 2026, [https://visualstudiomagazine.com/articles/2026/01/26/what-a-difference-a-vs-code-fork-makes-antigravity-cursor-and-windsurf-compared.aspx](https://visualstudiomagazine.com/articles/2026/01/26/what-a-difference-a-vs-code-fork-makes-antigravity-cursor-and-windsurf-compared.aspx)  
4. Advanced Antigravity: Feedback Loops, Learning & Long-Term ..., hozzáférés dátuma: március 1, 2026, [https://www.nobleprog.mo/cc/advantigravity](https://www.nobleprog.mo/cc/advantigravity)  
5. Synthesizing Procedural Memory: Challenges and Architectures in Automated Workflow Generation \- arXiv.org, hozzáférés dátuma: március 1, 2026, [https://arxiv.org/html/2512.20278v1](https://arxiv.org/html/2512.20278v1)  
6. Mastering Agent Skills: The Open Standard for the AI Revolution, hozzáférés dátuma: március 1, 2026, [https://antigravity.codes/blog/mastering-agent-skills](https://antigravity.codes/blog/mastering-agent-skills)  
7. Get Google AI Ultra benefits, hozzáférés dátuma: március 1, 2026, [https://support.google.com/googleone/answer/16286513?hl=en-MP](https://support.google.com/googleone/answer/16286513?hl=en-MP)  
8. production agents ≠ demo agents — the context management pattern that finally worked for us : r/AI\_Agents \- Reddit, hozzáférés dátuma: március 1, 2026, [https://www.reddit.com/r/AI\_Agents/comments/1re2g7r/production\_agents\_demo\_agents\_the\_context/](https://www.reddit.com/r/AI_Agents/comments/1re2g7r/production_agents_demo_agents_the_context/)  
9. Hogyan használja a ChatGPT a Google keresési eredményeket: amit minden SEO szakembernek tudnia kell, hozzáférés dátuma: március 1, 2026, [https://360-marketing.hu/blog/chatgpt-vs-google-kereses/](https://360-marketing.hu/blog/chatgpt-vs-google-kereses/)  
10. Learning AI : r/programmingHungary \- Reddit, hozzáférés dátuma: március 1, 2026, [https://www.reddit.com/r/programmingHungary/comments/1rbed3v/ai\_tanul%C3%A1sa/?tl=en](https://www.reddit.com/r/programmingHungary/comments/1rbed3v/ai_tanul%C3%A1sa/?tl=en)  
11. Synthesizing Procedural Memory: Challenges and ... \- arXiv, hozzáférés dátuma: március 1, 2026, [https://arxiv.org/abs/2512.20278](https://arxiv.org/abs/2512.20278)  
12. CodeMEM: Deterministic Code Memory Framework \- Emergent Mind, hozzáférés dátuma: március 1, 2026, [https://www.emergentmind.com/topics/codemem](https://www.emergentmind.com/topics/codemem)  
13. Prompt Fidelity: Measuring How Much of Your Intent an AI Agent Actually Executes, hozzáférés dátuma: március 1, 2026, [https://towardsdatascience.com/prompt-fidelity-measuring-how-much-of-your-intent-an-ai-agent-actually-executes/](https://towardsdatascience.com/prompt-fidelity-measuring-how-much-of-your-intent-an-ai-agent-actually-executes/)  
14. Synthesizing Procedural Memory: Challenges and Architectures in Automated Workflow Generation \- arXiv, hozzáférés dátuma: március 1, 2026, [https://arxiv.org/pdf/2512.20278](https://arxiv.org/pdf/2512.20278)  
15. Community | Antigravity \- Antigravity Codes, hozzáférés dátuma: március 1, 2026, [https://antigravity.codes/community](https://antigravity.codes/community)  
16. 500+ Agent Skills for Claude Code, Cursor, Antigravity & AI Coding ..., hozzáférés dátuma: március 1, 2026, [https://antigravity.codes/agent-skills](https://antigravity.codes/agent-skills)  
17. Skills, Not Vibes: Teaching AI Agents to Write Clean Code \- DEV Community, hozzáférés dátuma: március 1, 2026, [https://dev.to/gde/skills-not-vibes-teaching-ai-agents-to-write-clean-code-3l9e](https://dev.to/gde/skills-not-vibes-teaching-ai-agents-to-write-clean-code-3l9e)  
18. Antigravity Rules & Custom Instructions | ESLint, TypeScript, Python ..., hozzáférés dátuma: március 1, 2026, [https://antigravity.codes/rules](https://antigravity.codes/rules)  
19. vulcan-mcp | MCP Servers \- LobeHub, hozzáférés dátuma: március 1, 2026, [https://lobehub.com/pt-BR/mcp/engenharia-dev-vulcan-mcp](https://lobehub.com/pt-BR/mcp/engenharia-dev-vulcan-mcp)  
20. AI Agents: Architected Memory Systems For GSCP-15 Agents, hozzáférés dátuma: március 1, 2026, [https://www.c-sharpcorner.com/article/ai-agents-architected-memory-systems-for-gscp-15-agents/](https://www.c-sharpcorner.com/article/ai-agents-architected-memory-systems-for-gscp-15-agents/)  
21. Google Antigravity Training in Thimphu \- NobleProg Bhutan, hozzáférés dátuma: március 1, 2026, [https://www.nobleprog-bt.com/google-antigravity/training/thimphu](https://www.nobleprog-bt.com/google-antigravity/training/thimphu)  
22. Complete Guide to Google Antigravity | Tutorial & Documentation, hozzáférés dátuma: március 1, 2026, [https://antigravity.codes/tutorial](https://antigravity.codes/tutorial)  
23. Agentic AI vs. generative AI \- Red Hat, hozzáférés dátuma: március 1, 2026, [https://www.redhat.com/en/topics/ai/agentic-ai-vs-generative-ai](https://www.redhat.com/en/topics/ai/agentic-ai-vs-generative-ai)  
24. Antigravity Virtual Memory (VSZ) Bloat \- 1.4TB per Process \- Gist \- GitHub, hozzáférés dátuma: március 1, 2026, [https://gist.github.com/ecast162/d41d18addf1307350092787e135b36df](https://gist.github.com/ecast162/d41d18addf1307350092787e135b36df)  
25. Connect to SSH Host.... Crashes when attempting connection to ..., hozzáférés dátuma: március 1, 2026, [https://github.com/devanshug2307/antigravity-discussions/discussions/43](https://github.com/devanshug2307/antigravity-discussions/discussions/43)  
26. From Runes To AI Agent Infrastructure: $CRYPTOBURG Lands on Gate.io Crypto Burger Ushers in the “Agent Economy” Era on Bitcoin | MEXC News, hozzáférés dátuma: március 1, 2026, [https://www.mexc.co/en-NG/news/798048](https://www.mexc.co/en-NG/news/798048)  
27. What Are AI Agents? Types, Examples, and Benefits | Triple Whale, hozzáférés dátuma: március 1, 2026, [https://www.triplewhale.com/blog/ai-agents](https://www.triplewhale.com/blog/ai-agents)  
28. AI Agents vs. AI Assistants \- IBM, hozzáférés dátuma: március 1, 2026, [https://www.ibm.com/think/topics/ai-agents-vs-ai-assistants](https://www.ibm.com/think/topics/ai-agents-vs-ai-assistants)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAXCAYAAACBMvbiAAAB+klEQVR4Xu2VTSuFURDHRyhCIoWFko18AKQsbCwsSFIkZcnC2jewkyILKUmyk1LsLG5ZWtsoG4mFhSwo5GX+z5m5z5zxdK/yUur+6t89M+fcc+bMnHMeohJ/SyVrRn4LMeYdP00P645VxrpgDcbdeXZYc95p6WS9i55Z1XF3wj6lYzZdH4C/S9oVrFfxLbPGWSti38qYTJZYDxR2BNbFtmDHG8ZGGz6licJCtcbn5wDIWNZGE3opTGIH6O4VpNvaAIHD1yd2q9g2mCvTBhNUpDxPrBvnq2KVG/uMPgcD4MtJu0bs5nxvnBkc6ILlaaAwwR6FnY6yBuwAwWdKge/R2CjbpLTbWGumr2B5QD+FCQ9ZB+KbEl+9DhI7q/4+SOwe9i6Fw6tMU5HygGH6PCE4pXiyrwaThS9PO4X/4MZGb5EGc2ydzLb4O8T+TjDXlJYH2cZ4HAkomrNbOrG4RYNBsADtl7Q7T7FgUB5IOWKdGHuRwpOQUEeFgxkSG1c0a1H4cDCzQDaQFQsykTM2kqEbTnijOFqA24WFNL3zYnvgm/VOAefEf598MLhAuuGEEUrrqCBA+9rqA2e/NXjAsgIEuDno9/gyrZIpk7JAYeJL+d2KuxMaKfThpkFo46HzIJvn3in4A2w/J78CbqYvj6WFwrNxT3E1SpT4v3wAfiiJht4p+f4AAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAXCAYAAAAV1F8QAAABjElEQVR4Xu2UPyjFURTHv5IiSVEk6s3KppTBaFAYUAY2IysyKGUxyiJSstoNyvBmBotByqBIKSmhKH++53fvfe/c032/5+3vU5/63XPPfef+zu/eB9QBBumYDRpaaYcN1sINXaB99Is2xtMZTfSXNtgJYZVe0AHaTAv01McDw/RHjTfoM32gc3SGXsMVGS2nxcgPSoL2LMoATuidGvcg3ojQTq9MLEIWrNN9uJ2lXruIuFAbPVJj4R3ptSWk0IQNGg7oqxr3w7UssIaclgX+U6gbrqWBIm3xz1VbFpBCx/SJLsKdKPuNhCW4uUu6ouKfqNKygBSSV9fI7g9NLMUm4pbtwa3dUbFc7pFzHzydiFsmGwubm6VTai5D7o6lCFdIjnElbMskXy5zQO5ZiV64BH2ihFsfr1Rom46oseTZfOlKiXCadnWQfPh4ii56bmKpQo/qOeMF7o8wUIBbNK1imm+kv11u6wRZJMf2zSsLxqOMMtKyIRv06MMwTyfVXM2k7pdmC26jy3aiTp2MP3rwVO8Cm59yAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAYCAYAAACIhL/AAAABwElEQVR4Xu2WPS9FQRCGR0JCfBXERyhEp1ZJ/AANBY0EtUavlfgHStGKRHRav0CjkohEglKChoJE2Dezk2zeO+fu3nsQhSeZ5N53Zmfn7O6ZsyL//D02WMgwHWyQxVLWg11FWyCfx36wFRYLuA42yWIzzoO9B5uK/zui9hlsLGrMkmhMFQOi4z06RX2Ypym9ooEH7IhYkV4i6D2kjQT7iD6zKnaDnbKY0iWa4IwdCTgviNkmfSvYLWnMnTQvsFvUj9V0eZXq1TH6RGMwWQrGrpHG5AoEyLPJIlgVHXzEDqJfNA6JDDs/w4nmUVLgYbAbFsGb6OBRdhDz0riCtu05SgrELjTE2N43OBxOROP2Em0xajlKCpwVJ8ZW4JEdDvYgaWN1n9qh7QLRIHnbPOZE47jXLUc9R9sFWu/LraD1M37Lf3yLwbP4kxvojfB7n6MZqUhKlBRYeVyGRB1ek74Q9WGlPUrbzINUTJ6ANnPJooECbBvvg73E3+iROdCmvEZtjR25kBP2FLXxJM4oafhtsSP5T12O7KeuDji7SM6XhVbAZeGYxe8E90BuQaUUX7fq8msX1jq0euWfkBpX/n9yfAFfR39ejJ9/ZAAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAXCAYAAACBMvbiAAACFklEQVR4Xu2UwUsWURDAR1IwskQMM1D46KZXURA8hR061MECOwhe+w86R3QNFE/eRDwJ3YIOHT7wVmcvgdAhivAQgnpQ0t7vezPfzo67e5Ig+H4w7M7M2/dmZ+aNSI9/y0CSVX02sRQN181ckt9J+pIcJHlUdnfZTvIyGo2JJH+SXOrzTtld4r3kdcjr4MM2pe/9Uuz5LsnzJGuqH+qaK5AuFlhah1Uf7a7I4Mf+VHXWcdiM6nfVP6Q6nLh3g4zdjEYgejb4FOz7Sb4HGxt/dPq65G+t9vdV98HEPZaloTyLkjfYCnZ07NQe5lV/0F2RGXPvtySvuedsPjNktrY88ESag7H6f1GdTLYk139QfR6a94W+TybZcL7a8hgLUh3MB7UTLJyrTjlp9huS/3pX/Yb11Y7kfjJWpKE8BmXg43aw2+EWDO+I/TWMqK3u+hqxPC3J352prwSzAael8FmSb2qbVZsFQ194sP0MtsgPKfa2m0oSkKrb1pkrvySndlqKnuG6wqnqEQuyDsqDGJR/z+lvpTijFq62P4QNqg5tCoZskBUPmWg7ncxbK3S4kKsbor9yuo2A285mM8rPHg99EnsiBsMFeuz0zoa+8zclX9EIa944nQHGt/FA4Obgj8QyMThLZXooeVOmJc/P3ungUALiFhxLXhsbGijP12hUYgNX/fS1wiyqypYxLvmnjqSY8D16/N/8BeveiFEHWyf/AAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAABSUlEQVR4Xu2WvUoDQRSFr71NEASbtClTWNgkkMI2LxDfw4hgFSyCja+QQgiYh1jyDEkj2vgCqVKJ6D3ZHfZ6nI2zwQ1ZmA8OzJw7P3s2w2xEIpFIWW5UQzZL8KhK2CTOVV8l1FGdqt5Vn8ZH32nD1BShXYNgM8xPyGf6qjfysKdv7xfVlemfSTpuYrxfHIt/sVA+JCwI1sdbZs+3d1t1b/qVBxmpLiQsCB6iQV5REDzTzPQrDXKimmftkCA9NqQ4COiZdqVB1qqjrB0SxMe2IBYX5DlrO/1glyDXqq7p1zIIxi/I21eQfz1aK8mPlKOWQewHyQnz8dFC+zIf+id7DTJQtdgkDuIXwTWKQXdckHwBqAgcM9SXXAjgVtK5Yy4QTUnHPXEBIB2KfERwrVpeVQ/kOeyRcvPxV2Qb9uXw3pC9jexYnyKRKvgGe0WScMLNIoAAAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF4AAAAXCAYAAACChfjKAAADfUlEQVR4Xu2Yz6sOYRTHj1DkVyQSdSkpRRZKka2ywIbwH1iwshGlbsk/gFKim4VEsqFQFhMlsZYSC1JCKKGQH8/nnufc98x5Z+beea+FbvOp0zvzPed5Zp7vzDzzvCPS0dHR0THVOZLicYp1KWalGEpxJ+uR6yn+5LgQcoMwX7SvOm5J73jPU0wvp0eZmeKd9Or2ltN9zEnxKsUv6bVZWKoogy9W90W0LfD70eXYtzD9Ua6tBIOtscXdUoXyKcU5t882WluWSHnQRBXULMrbGG5tFoxVqOlom5zGOZ11+3UsS3FTtP1IyHkepihE6+aWU6Ogf41iYqVortYjjD8uauSeFNPK6VG2Sb9B1KFtDnobXkp/v7ArxY8Ua5y2SrT2tdNupPjg9mGjaN2MoEcw/qJo+6pzAMZ4WwYzHr6J5tfGBGD8zigGnkj1yaEVUWxBnfGnRPUXQUfz9VXHn5d1Ll4TZjx1dTfQftELXshgxqNPyvg4YAONqzoodcZzp/EE8g7w+PNgrmY7TouYg34p6BEzHqh/6nLG2/xbSHvjmVLJNU41V0VfUAdFH/E4mLrO6y7IRKkzvgp7yfHoA8axb+YZZjwLhia88fRJGz898S4ZztuFNBvPzUd/FseyPuLq+sD4o0GLjf4H4+2xtXfQeMbTdxPeeKYT2hzqpeWM6CoPCmln/ArR47MgiE9tI7zA/CDHM369lJdTdcH04Jmo8Uw7DMLOB/6l8fA7xXe3798vhTQbX+UN0Af5oZgAu6qeQrQBJwds/xzL9jDjB2Uixu9O8T6K0jP4Wo1eBD0SjR8WbbdUdFrb6nJFzrU1nj7Iv4mJ5TnxOeh2pcx4ewIiaHHl0YbxjGd9/ixofhBVBtuq5nDQI9H42dK7kPH9UMhgxtvSti/P1SUR/3DY+tNg7qsyCO1AFFvQZPxQintRlPIgWInEdfwG0T4XBz0SjQe7wS4Hvch6W+NZtJA/HxPAcsfPvQyYYh5xg7kVjT9Sxr6sTQb7qx+xu68q7ru61Vmj3uBiVS0NIydEx+4/Q2wX7Y8b0vMg6zxNHvOlakl9WjRXu5ykMUtIvkMQFO8oVSj8fSfHY0iwHV+WE8HmYPvu4b9t2NTGnRgNtziZawzOFf2K6CD5ptOEHZ+7m2OzzcrO8NNuIZq388Qn9iGeVwxuqi25tqOjo6Ojo6NjCvIXdEZTrSyvKScAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFMAAAAXCAYAAAB3e3N6AAAC90lEQVR4Xu2YzctNURTGl1Dkq6SklPeViQwMfJSSgY+kMFH8CQyYEGJuwMBIKXl7MzAgmZhKJwMGxiJRSBRJKQbkYz93r+eedda7z7nnXudS2r9addaz9jl7n3X33mufK5LJZDKZUTgW7Jfaj2Arq+E+t6VsN+Viw/BQyuecdzGyUco2X4MtroZ7zA32Xsp2B6vhsbA9WOFFcjfYIePflziwA0YDn4JdMT6uoQ0LfqxTxkf/T4wP0DfGMEv9JerbHxmJhLbZaBjPZeN3xREpfzBYUYkqCyUGTzidN5Fdzgd4UWhbnN4EB2XhGCaNBv+w8UER7I3x7wT7aHywQeK9c5zeJbXJXCszEwdeqbZC/cfqe2ofXANe/osXJT5nWq85JiTGclZ1ztZU34tU3+/0Lkn12+dcsG1OeyfxpuXqpxIOoGE/awvaf/aiRJ2z7rj668twj9OqY6kv0GtsERbO8utOT7HDCy1pTKaHy/en0eDXzahUkutAW8x6D/Tven1Nfa4KwmRu1Riu0dbCZD5yuueqpH+MNgyVzGmJN6wy2t9IJp8zKJn7NNaUzFQfFrwb2u32gRa0TiYqIxr7o9H/lsw/oVUyefyY7wMSdS5DyyjJxH7ssT8Wk7a6DFd0FCYm7ValRakXTu+Sgc/nmW220VCYWIBQHFJJg/bCiw2gWNXNcO5fm9Svq+YoPiD1UqzmKGLjItVvHxQczDoeOchLc31U6pNpz4PLgl0wvueSzHwOK/NO9VkA/TkTybZFEQd9f87ECQD3YhxNoI+LUp08bWlMJr4a0CBlhC+IwzvBV5NPDGYdNCzJFFwB64x2RuJXkeVmsA/GZ//2/LhGNbst4evNf02l4L5cOH0QHMcDHwD8YkiZ39uWqo5jBwzXXHJkj8TEFE63TEi8916wp8G+SUyyBwPGs/AfANqfrIZ77JUYuyFxUjyvhmthfZhweh0oemj/NthrNYwN2liZJ/Ecl+kA7K+TXswMD5b9My9mRiN1Rs1kMv+M32EgAeIby/g+AAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHQAAAAUCAYAAABcbhl9AAAC7ElEQVR4Xu2YzctNURTGH6HIV5lI6I2ZIgMUwkwZYEJJ/gCKkUJE3fIPGCil9GakDMwUZXBLoQyMZKSQDBiIUMjHfqy93r3OOvuc23tQ3nP3r1btvdY+5567n73X/gAKhUKhUCj8CaeDPQq2Lti8YBPB7kS/52awn9GuupiyCanN52CLq+EaR4O9RHrmWzVc4zZS21fB7gVbj+o7aKyrqe8QxgAKZzuCdrfSQngX7Iqps0yfZT/k+VmxviTWV061aOYaZJCw/QoXszyEtPnkA4GNkFhuME5CYqd8oG/wz5+HCHQASQzLLkhnWNiOvq3Gx/oRUydDyEwaBQVdDXnHLRdTdkMySRdBFyEN2F7DP7/XOx1PkO8I+oaxvDbW2amWs9GfGygWCro82HPkf4swfZIugi5EEXSKpo6gj+skORHrG1L4N5rSR6VdFXQ7pD1no2V+sEux3EXQi5DYWKTcG8HeBDsW7Cvqa2hTB1qhKQjLFMWiglKoNlRQwvY+TQ8gazJp+h4V9ALkXTQOpMfRvzM17S/s8DPOxz8/6eq5DpyOoKOygBX0OuQZzkrltSk3fU9OUNqO6H+Qmo4XnB3sAF33mjrwXwm6DPLMINa5WdoXy6Tpe9pS7lxI7LsPONjODoZR9t/Bs6dniKo4LOfOh1ZQFW5NClf8frPksYKSL8F+xDLPnpYughKetxk/7AOGGS0oz3v8gx+c/1n06wfrjPXQx7Zkc6x74XSXu8D5PV7Q40gD5G8JOkR7fMajqe2y83PnagXUzvXQp+dOPZf6cyg3WDrT2vCCzoG8j88y5Vq6CsoYbZUP9Ane9tjZMwH507z1UVQsXjAoB6PPwt3yW1PX5+z6l2M25Du4mbE8RX0w6Dv1uGTZBokxK1iYRt/H2KAa6h/sIB5VPkbjn95TaSEshcS4DulalEuj9yEbD73GO1kN19A1lpcGmtp5CUC2BDsXy4Qxvtve0b5AmpltxivD3PcWCoVCoTBdfgH84gOa+Qo9cAAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGcAAAAUCAYAAACQ9yOWAAABaUlEQVR4Xu2YP0sDQRDFx05QFJJCBCs7qxRqEbC11MbCj2BjJYhB8IsIFunEwk9gkcrG2tJG7CystBH/7GRnsrMjd+dGJEXeDx7svLm9Yh/Z2w0RAAAAMDl6QSfeNFwHfYkuXE/ZoPTMW9BC3gYlXFJaTFZVOC9B56bmMXuWPYrvmJF6UeqV0RNgLOapOpxtij0LB8Be13hcH5iaGQQ9OQ8UUhfOPf0Mh2FvIOM1qddH3cip+PprAmNQF45ueR72+LvCHEndSe0h/D5sbX+kKZxXb1IeWl/Gy6k9RMPZcj4o4L/D2XE+KGCS4SxRnPcbzcqcqaIpnHdvUh6OhrCa2pnvDwoWhNNAXTh8FNYQLOw9yHhTah+CntbmnA8KqAvnkKrD0XuN3nv8Pecm6NN5oJA2xcU98w1KC8+XUWVfPMtV0LOpdd6u8UAB+iF/NOLaHwBa4t+Jqraq26APiv+98TPHeRsAAMAU8g3NS3LMPBjEngAAAABJRU5ErkJggg==>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADEAAAAUCAYAAAAk/dWZAAAB0UlEQVR4Xu2WvUvEQBDFR7BQ7CwUsdLOWlQEW0F7QcE/wMbeSrhGsLYUrAULO0GsAjaCtVgJKn6ghYKojfgx73aGmx03d2cudvnB43JvZsO+ZLMJUUVFRYqMdcvaZi2zFpws+6xv0Y6rpbhmvVJjzExcjuilRt8nhbEDrGPWjak9Sg2CX+fFNHjdaRPzTCGogmN47XBF4XyXzrfUWJsU+sbjUh09RxIUkNiDq9Etx7P0+wRd4k07PwUmcEChv8fVlAfWGhUIgUni5J4j1qT5f0bpE8DLvJkAExim0F+LS3VGWEtUMESKKYqXDdDl5YH37s0EmAD4YH3ZgnBI4c6WEkKXiAfemzcpP5xHQ6xS6MeVt5zIbzshhozmog5hj7XlTSovBJYv+nHlFUxkTI7/GgKK0Lsw6gtUXghwTvEYbJVKOyGagncEmnRHssDHevYUCYHdDGNwB/Bu2DC1jkNcUH6Tvmw88DCuFTYEwLh7CgEQROk4RLOrqg+kB96KNxP4ELsUxtqlBP41hD4veOkpi+K1Yp5CX5/xBsXzu8u6+BPOB/g0Qg1zyaVZCNBPoX4q8hNLgR791sEXQGZq+NxR9A5g2aL3Sf5j99E7kKeKirL4ASV0tz46os+xAAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAAUCAYAAAAgCAWkAAAB9klEQVR4Xu2WTSuEURTHj7BQJBZeSg0bsqG8loXmO1BKki9gQ7GdjZUvIIl8D2XyJZQsUNiRBQvycv7Oc8x5ztx5XqbYmF/9m+65/3vn/u/c5z5D1KDBv2KUdcK6YW2aeoE1bNqZWGd9RnpnDcS7a3LN2iPxt7NmWLesfmtKYJoq3zkX1XpZT6yJqG8yqgOEfYjqENqqb7AjS9pgzkiMC6ZWC4TRiVWrMUdt1kj8pXj5hwuqDqOg/uyL2E102J8W6MLSQJgV1j6rGO9KpIdk/jvfYWijnGFwVkML1x1POy7wYUPyck61F2q5p7AnGAbssOZdDZNgAM5vEvWG0Q1s8h2OY8oZxoMvgPnDdwRAmFNWmbVFMi7tmcGvHToNecDYF5K5VEGOSMwF3xEAYQZNe4hk7Kypef4sDK5WGLNezSEw/tEXDR2UHGaR4ovEmorWQBmOWSeJCbdIVrp8gZIXqqgHwTwIA72SeA4pZ5hWEkOzqeFiSLoAtknGHLh6ljA6tuTqljKJJ9cFgAf+Lfq0XLn2MmvEtDdIJp0yNb08cPWmgbc+vNjIEGWqIwzOt+6mlxJ6aFuoekK90XBk00BwDdTt+vSFGQqjG4YLIAaMPoAK7xrLJWvX1fpIvHiT6zi/sDTs/0IV/pvhyI+xxivWKp9Vgwa/zRd+tafsWZlb0AAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC4AAAAUCAYAAADyWA/8AAAAvElEQVR4XmNgGAWjYGSAciA+DcQ6QMwBxPJAvBMqPqgByIH/0fAeFBWDFIAcXgvEs4A4BIgZUaUHLwA53BddcCiAIe3wVUD8CoizgfgXwxBK45VoYqAMOh9NbEiAJwwQx+PLqGJALEkk5oHqoSoAld3o4AADxOEgS3GBAXW4NAPEgZ/QxO9CxfE5fECBOAPEgdPRxL9BxQc1eA/E3Eh8UJUPcnQwktigBKAMCCoCv0AxyNE+KCpGwSgYmgAA6AMmUtuosV8AAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADcAAAAUCAYAAAAp46XeAAAA2ElEQVR4Xu2WoQoCQRRFH4hgsBnEbjH5HQaTRrN+giIY7SKC2WbwqywbTWa9j2HZ9TLuzgbxDcyBE/bOC3MZmB2RRCLxbzZwzSHowhe8wCOck6Ni1BZXcRvP9ZUby+cMOyxGbZKfjq/cCi5hi/IZPFNmkqpyN9ihTOcflJmlqpyPJ2xzaJUm5Q5wwaFlQsvpaelcVISWO8GMwy/oBTRo4M8ILaczesGEEFW5vriZPS9YJ6TcVOpnTNITt/EdL5TYSmTl9L2oG76X1G/9jzH6UtG1CS8kEola3mzzOAzF2lTWAAAAAElFTkSuQmCC>