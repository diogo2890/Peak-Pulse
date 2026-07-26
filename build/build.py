# -*- coding: utf-8 -*-
# Peak Pulse site generator. One template, five native language versions.
import os, pathlib
from urllib.parse import quote
ROOT = pathlib.Path("/home/user/Peak-Pulse")

PATHS = {"pt":"/","en":"/en/","fr":"/fr/","nl":"/nl/","ar":"/ar/"}
BASE  = "https://peakpulse.pt"
WA_NUMBER = "351920484417"   # +351 920 484 417

def wa_url(msg):
    return f"https://wa.me/{WA_NUMBER}?text={quote(msg)}"

WMI = ('<span class="peak"><span class="ini">P</span>EAK</span> '
       '<span class="pulse"><span class="ini">P</span>ULSE</span>')
def wm(cls, tag="span"):
    return f'<{tag} class="{cls}">{WMI}</{tag}>'

SYM_MARK = ('<svg class="mark-sym" viewBox="0 0 200 120" aria-hidden="true">'
  '<path d="M38,120 L100,0 L162,120" fill="none" stroke="#16181C" stroke-width="7" stroke-linejoin="miter" stroke-miterlimit="10" stroke-linecap="butt"/>'
  '<path d="M100,15 L118,52 L82,52 Z" fill="#8A6A2E"/></svg>')

SYM_FRAME = ('<svg class="frame-mark" viewBox="0 0 200 200" aria-hidden="true">'
  '<path d="M38,160 L100,40 L162,160" fill="none" stroke="#16181C" stroke-width="7" stroke-linejoin="miter" stroke-miterlimit="10" stroke-linecap="butt"/>'
  '<path d="M100,55 L118,92 L82,92 Z" fill="#8A6A2E"/>'
  '<path d="M14,160 H186" stroke="#8A6A2E" stroke-width="2.2" fill="none"/></svg>')

SYM_MISSION = ('<svg class="mission-mark" viewBox="0 0 200 200" aria-hidden="true">'
  '<path d="M30,168 L100,28 L170,168" fill="none" stroke="#E7E0D2" stroke-width="4" stroke-linejoin="miter" stroke-miterlimit="10"/>'
  '<path d="M100,52 L122,96 L78,96 Z" fill="#C9A45B"/>'
  '<path d="M18,168 H182" stroke="#C9A45B" stroke-width="1.6" fill="none"/></svg>')

def eyebrow(num, label, dark=False):
    cls = "eyebrow on-dark" if dark else "eyebrow"
    return (f'<p class="{cls}" data-reveal><span class="ey-rule"></span>'
            f'<span class="ey-num">{num}</span> {label}</p>')

# ---------------------------------------------------------------- content
C = {}

C["pt"] = {
 "lang":"pt","dir":"ltr",
 "title":"Peak Pulse. Presença online que traz clientes",
 "desc":"A Peak Pulse constrói e gere a presença online das marcas. Uma coisa de cada vez, pela ordem que dá resultado. Resposta em dois dias úteis.",
 "org_desc":"A Peak Pulse constrói e gere a presença online das marcas.",
 "nav":["Serviços","Diagnóstico","Método"],
 "cta":"Pedir um diagnóstico",
 "hero_t":"Ser encontrado. Depois escolhido.",
 "hero_s":"A Peak Pulse constrói e gere a presença online das marcas. Estratégia, identidade, site, SEO, conteúdo e publicidade. Uma coisa de cada vez, pela ordem que dá resultado.",
 "hero_n":"Resposta em dois dias úteis",
 "sit_e":"O ponto de situação","sit_t":"Três coisas custam clientes à sua marca todas as semanas.",
 "sit":["Encontram a sua marca, mas ninguém percebe em três segundos o que vende.",
        "O site recebe visitas que nunca se transformam em pedidos.",
        "Publica com regularidade sem saber o que isso lhe traz."],
 "mis_e":"A nossa missão","mis_t":"Construímos presença que se paga.",
 "mis_p1":"A Peak Pulse existe por uma razão. Uma marca pode ser excelente e continuar invisível, e uma marca invisível perde para outra que apenas aparece melhor. É essa distância que fechamos.",
 "mis_p2":"Trabalhamos à vista, uma prioridade de cada vez, e ligamos cada passo a um número que já lhe interessa. Sem ruído, sem métricas de vaidade, sem contratos longos para nos escondermos. Quando o trabalho deixa de compensar, somos os primeiros a dizer.",
 "prin":[("Ordem antes de ruído","A coisa certa, na semana certa. A sequência é quase todo o resultado."),
         ("Provas antes de promessas","Medimos o que entregamos e mostramos os mesmos números que acompanhamos."),
         ("Fica seu","Cada documento, cada conta, cada recurso fica em seu nome.")],
 "svc_e":"Serviços","svc_t":"Quatro áreas, nunca todas ao mesmo tempo.",
 "svc_i":"Começamos pelo que produz efeito mais depressa no seu caso. O resto vem a seguir, quando a base estiver sólida.",
 "groups":[
   ("Estratégia e performance",["Estratégia digital","Publicidade paga no Google, Meta e LinkedIn","Análise de dados e retorno do investimento","Otimização da taxa de conversão"]),
   ("Visibilidade e conteúdo",["Otimização para motores de busca","Redes sociais","Conteúdo editorial, newsletters e vídeo","Marketing de influência","Reputação online e avaliações","Relações com a imprensa online"]),
   ("Criação e técnica",["Sites e comércio eletrónico","Identidade de marca e normas gráficas","Design visual","Integração de CRM","Inteligência artificial aplicada à relação com o cliente"]),
   ("Crescimento e fidelização",["Campanhas de email e automação","Funil de aquisição","Experimentação e medição"]),
 ],
 "dia_e":"O diagnóstico","dia_t":"Antes de qualquer proposta, um documento.",
 "dia_b":"Uma auditoria completa da sua presença online. O que funciona, o que bloqueia, o que fazem os concorrentes e por que ordem corrigir. Fica consigo, trabalhemos juntos ou não.",
 "dia":["O estado medido do site, do SEO e das suas contas","O que fazem os concorrentes nas mesmas pesquisas","As correções a começar esta semana, por prioridade","Um plano de 90 dias, com os indicadores a acompanhar"],
 "dia_btn":"Pedir o diagnóstico","dia_label":"O que recebe",
 "brief":"Duas páginas do diagnóstico, na horizontal, luz rasante. Nenhuma imagem de banco.",
 "sui_e":"Situações","sui_t":"Quatro situações, o mesmo método.",
 "sui_i":"Vai reconhecer a sua. Nos quatro casos o ponto de partida é o mesmo diagnóstico, e os trabalhos duram no mínimo três meses. É o tempo de que os números precisam.",
 "cases":["Está a lançar uma marca e está tudo por construir","O site recebe visitas e não gera pedidos","É visível nas redes e invisível no Google","Já vende e quer industrializar a aquisição"],
 "met_e":"Método","met_t":"Quatro tempos, por esta ordem.",
 "stages":[("Diagnóstico","Olhamos antes de propor. O documento fica consigo, mesmo que não avance."),
           ("Plano","90 dias, por escrito, com prioridades, responsáveis e datas."),
           ("Produção","Design, texto, desenvolvimento, publicidade. Aprova e executamos."),
           ("Medição","Um ponto mensal sobre os números que decidem: pedidos, orçamentos, vendas.")],
 "clo_t":"Comecemos por ver onde está.","clo_2":"Ver os serviços","clo_f":"Lisboa. Resposta em dois dias úteis",
 "foot":["Serviços","Abordagem","Contacto"],
 "legal":["Privacidade","Cookies"],"city":"Lisboa","wa":"WhatsApp","wa_msg":"Olá Peak Pulse, gostaria de pedir um diagnóstico.",
}

C["en"] = {
 "lang":"en","dir":"ltr",
 "title":"Peak Pulse. Online presence that brings clients",
 "desc":"Peak Pulse builds and runs the online presence of brands. One thing at a time, in the order that pays. Reply within two business days.",
 "org_desc":"Peak Pulse builds and runs the online presence of brands.",
 "nav":["Services","Diagnostic","Method"],
 "cta":"Request a diagnostic",
 "hero_t":"Found first. Then chosen.",
 "hero_s":"Peak Pulse builds and runs the online presence of brands. Strategy, identity, website, search, content, advertising. One thing at a time, in the order that pays.",
 "hero_n":"Reply within two business days",
 "sit_e":"Where you stand","sit_t":"Three things cost you clients every week.",
 "sit":["People find you, and no one understands in three seconds what you sell.",
        "Your site gets visits that never turn into enquiries.",
        "You post regularly without knowing what it returns."],
 "mis_e":"Our mission","mis_t":"We build presence that earns its keep.",
 "mis_p1":"Peak Pulse exists for one reason. A brand can be excellent and still go unseen, and a brand that goes unseen loses to one that simply shows up better. We close that gap.",
 "mis_p2":"We work in the open, one priority at a time, and we tie every move to a number you already care about. No noise, no vanity metrics, no long contracts to hide behind. When the work stops paying, we say so first.",
 "prin":[("Order over noise","The right thing, in the right week. Sequence is most of the result."),
         ("Proof over promises","We measure what we ship, and we show you the figures we watch."),
         ("Yours to keep","Every document, every account, every asset stays in your name.")],
 "svc_e":"Services","svc_t":"Four areas, never all at once.",
 "svc_i":"We start with what moves fastest in your situation. The rest follows once the base holds.",
 "groups":[
   ("Strategy and performance",["Digital strategy","Paid advertising on Google, Meta and LinkedIn","Data analysis and return on investment","Conversion rate optimisation"]),
   ("Visibility and content",["Search engine optimisation","Social media","Editorial content, newsletters and video","Influencer marketing","Online reputation and reviews","Digital press relations"]),
   ("Creative and technical",["Websites and online stores","Brand identity and guidelines","Visual design","CRM integration","Artificial intelligence applied to customer relations"]),
   ("Growth and retention",["Email campaigns and automation","Acquisition funnel","Testing and measurement"]),
 ],
 "dia_e":"The diagnostic","dia_t":"Before any proposal, a document.",
 "dia_b":"A complete audit of your online presence. What works, what blocks, what your competitors do, and the order in which to fix it. It stays yours, whether we work together or not.",
 "dia":["A measured view of your site, your search visibility and your accounts","What your competitors do on the same searches","The fixes to start this week, ranked by priority","A 90 day plan, with the indicators that will be tracked"],
 "dia_btn":"Request the diagnostic","dia_label":"What you receive",
 "brief":"Two pages of the diagnostic, flat, raking light. No stock imagery.",
 "sui_e":"Situations","sui_t":"Four situations, one method.",
 "sui_i":"You will recognise yours. In all four the starting point is the same diagnostic, and engagements run for three months at least. That is the time the numbers need.",
 "cases":["You are launching a brand and everything is still to build","Your site gets traffic and produces no enquiry","You are visible on social and invisible on Google","You already sell and you want acquisition to scale"],
 "met_e":"Method","met_t":"Four stages, in this order.",
 "stages":[("Diagnostic","We look before we propose. The document is yours, even if it stops there."),
           ("Plan","90 days, written, with priorities, owners and dates."),
           ("Production","Design, copy, development, advertising. You approve, we deliver."),
           ("Measurement","A monthly review of the numbers that decide: enquiries, quotes, sales.")],
 "clo_t":"Let us start by seeing where you stand.","clo_2":"See the services","clo_f":"Lisbon. Reply within two business days",
 "foot":["Services","Approach","Contact"],
 "legal":["Privacy","Cookies"],"city":"Lisbon","wa":"WhatsApp","wa_msg":"Hello Peak Pulse, I would like to request a diagnostic.",
}

C["fr"] = {
 "lang":"fr","dir":"ltr",
 "title":"Peak Pulse. Une présence en ligne qui amène des clients",
 "desc":"Peak Pulse construit et pilote la présence en ligne des marques. Une chose à la fois, dans l’ordre qui rapporte. Réponse sous deux jours ouvrés.",
 "org_desc":"Peak Pulse construit et pilote la présence en ligne des marques.",
 "nav":["Services","Diagnostic","Méthode"],
 "cta":"Demander un diagnostic",
 "hero_t":"Être trouvé. Puis choisi.",
 "hero_s":"Peak Pulse construit et pilote la présence en ligne des marques. Stratégie, identité, site, référencement, contenu, publicité. Une chose à la fois, dans l’ordre qui rapporte.",
 "hero_n":"Réponse sous deux jours ouvrés",
 "sit_e":"Le constat","sit_t":"Trois choses vous coûtent des clients chaque semaine.",
 "sit":["On vous trouve, et personne ne comprend en trois secondes ce que vous vendez.",
        "Votre site reçoit des visites qui ne deviennent jamais des demandes.",
        "Vous publiez avec régularité sans savoir ce que cela vous rapporte."],
 "mis_e":"Notre mission","mis_t":"Bâtir une présence qui se rentabilise.",
 "mis_p1":"Peak Pulse existe pour une raison. Une marque peut être excellente et rester invisible, et une marque invisible s’efface devant celle qui paraît simplement mieux. C’est cet écart que nous refermons.",
 "mis_p2":"Nous travaillons à découvert, une priorité à la fois, et nous relions chaque geste à un chiffre qui compte déjà pour vous. Pas de bruit, pas de vanité, pas de contrat interminable pour se cacher. Quand le travail cesse de payer, nous le disons avant vous.",
 "prin":[("L’ordre avant le bruit","La bonne action, la bonne semaine. La séquence fait presque tout le résultat."),
         ("La preuve avant la promesse","Nous mesurons ce que nous livrons et montrons les chiffres que nous suivons."),
         ("Cela vous appartient","Chaque document, chaque compte, chaque ressource reste à votre nom.")],
 "svc_e":"Services","svc_t":"Quatre pôles, jamais tous en même temps.",
 "svc_i":"On commence par ce qui produit le plus vite un effet mesurable chez vous. Le reste suit, quand la base tient.",
 "groups":[
   ("Stratégie et performance",["Stratégie digitale","Publicité payante sur Google, Meta et LinkedIn","Analyse des données et retour sur investissement","Optimisation du taux de conversion"]),
   ("Visibilité et contenu",["Référencement naturel","Réseaux sociaux","Contenu éditorial, newsletters et vidéo","Marketing d’influence","Réputation en ligne et avis","Relations presse en ligne"]),
   ("Création et technique",["Sites internet et commerce en ligne","Identité de marque et normes graphiques","Design visuel","Intégration CRM","Intelligence artificielle appliquée à la relation client"]),
   ("Croissance et fidélisation",["Campagnes courriel et automatisation","Tunnel d’acquisition","Expérimentation et mesure"]),
 ],
 "dia_e":"Le diagnostic","dia_t":"Avant toute proposition, un document.",
 "dia_b":"Un audit complet de votre présence en ligne. Ce qui fonctionne, ce qui bloque, ce que font vos concurrents, et l’ordre dans lequel corriger. Vous le gardez, que l’on travaille ensemble ou non.",
 "dia":["L’état mesuré de votre site, de votre référencement et de vos comptes","Ce que font vos concurrents sur les mêmes recherches","Les corrections à engager cette semaine, classées par priorité","Un plan de 90 jours, avec les indicateurs qui seront suivis"],
 "dia_btn":"Demander le diagnostic","dia_label":"Ce que vous recevez",
 "brief":"Deux pages du diagnostic, à plat, lumière rasante. Aucune image de banque.",
 "sui_e":"Situations","sui_t":"Quatre situations, une même méthode.",
 "sui_i":"Vous reconnaîtrez la vôtre. Dans les quatre cas, le point de départ est le même diagnostic, et les missions durent trois mois au minimum. C’est le temps qu’il faut aux chiffres pour bouger.",
 "cases":["Vous lancez une marque et tout reste à construire","Votre site reçoit du monde et ne produit aucune demande","Vous êtes visible sur les réseaux et introuvable sur Google","Vous vendez déjà et vous voulez industrialiser l’acquisition"],
 "met_e":"Méthode","met_t":"Quatre temps, dans cet ordre.",
 "stages":[("Diagnostic","On regarde avant de proposer. Le document vous reste, même sans suite."),
           ("Plan","90 jours, écrit, avec les priorités, les responsables et les dates."),
           ("Production","Design, texte, développement, publicité. Vous validez, nous exécutons."),
           ("Mesure","Un point mensuel sur les chiffres qui décident : demandes, devis, ventes.")],
 "clo_t":"Commençons par regarder où vous en êtes.","clo_2":"Voir les services","clo_f":"Lisbonne. Réponse sous deux jours ouvrés",
 "foot":["Services","Approche","Contact"],
 "legal":["Confidentialité","Cookies"],"city":"Lisbonne","wa":"WhatsApp","wa_msg":"Bonjour Peak Pulse, je souhaite demander un diagnostic.",
}

C["nl"] = {
 "lang":"nl","dir":"ltr",
 "title":"Peak Pulse. Online aanwezigheid die klanten oplevert",
 "desc":"Peak Pulse bouwt en beheert de online aanwezigheid van merken. Eén ding tegelijk, in de volgorde die rendeert. Antwoord binnen twee werkdagen.",
 "org_desc":"Peak Pulse bouwt en beheert de online aanwezigheid van merken.",
 "nav":["Diensten","Diagnose","Methode"],
 "cta":"Vraag een diagnose aan",
 "hero_t":"Eerst gevonden. Dan gekozen.",
 "hero_s":"Peak Pulse bouwt en beheert de online aanwezigheid van merken. Strategie, identiteit, website, vindbaarheid, content, advertenties. Eén ding tegelijk, in de volgorde die rendeert.",
 "hero_n":"Antwoord binnen twee werkdagen",
 "sit_e":"Waar u staat","sit_t":"Drie dingen kosten u elke week klanten.",
 "sit":["Men vindt u, en niemand begrijpt binnen drie seconden wat u verkoopt.",
        "Uw site krijgt bezoek dat nooit een aanvraag wordt.",
        "U plaatst met regelmaat zonder te weten wat het oplevert."],
 "mis_e":"Onze missie","mis_t":"Wij bouwen aanwezigheid die zichzelf terugverdient.",
 "mis_p1":"Peak Pulse bestaat om één reden. Een merk kan uitstekend zijn en toch onzichtbaar blijven, en een onzichtbaar merk verliest van een merk dat zich gewoon beter laat zien. Dat gat dichten wij.",
 "mis_p2":"We werken in alle openheid, één prioriteit tegelijk, en koppelen elke stap aan een getal dat u al belangrijk vindt. Geen ruis, geen ijdele cijfers, geen lange contracten om ons achter te verschuilen. Zodra het werk niets meer oplevert, zeggen wij het als eerste.",
 "prin":[("Orde boven ruis","Het juiste, in de juiste week. De volgorde bepaalt bijna alles."),
         ("Bewijs boven beloften","We meten wat we opleveren en tonen u de cijfers die wij volgen."),
         ("Het blijft van u","Elk document, elke account, elk bestand blijft op uw naam staan.")],
 "svc_e":"Diensten","svc_t":"Vier gebieden, nooit alles tegelijk.",
 "svc_i":"We beginnen met wat in uw situatie het snelst effect heeft. De rest volgt zodra de basis staat.",
 "groups":[
   ("Strategie en performance",["Digitale strategie","Betaalde advertenties op Google, Meta en LinkedIn","Analyse van data en rendement op de investering","Optimalisatie van de conversieratio"]),
   ("Zichtbaarheid en content",["Vindbaarheid in zoekmachines","Sociale media","Redactionele content, nieuwsbrieven en video","Influencermarketing","Online reputatie en reviews","Online persrelaties"]),
   ("Creatie en techniek",["Websites en webshops","Merkidentiteit en richtlijnen","Visueel ontwerp","Koppeling met CRM","Kunstmatige intelligentie voor de klantrelatie"]),
   ("Groei en behoud",["Mailcampagnes en automatisering","Acquisitietrechter","Testen en meten"]),
 ],
 "dia_e":"De diagnose","dia_t":"Vóór elk voorstel, een document.",
 "dia_b":"Een volledige audit van uw online aanwezigheid. Wat werkt, wat blokkeert, wat uw concurrenten doen en in welke volgorde u het aanpakt. Het blijft van u, of we nu samenwerken of niet.",
 "dia":["Een gemeten beeld van uw site, uw vindbaarheid en uw accounts","Wat uw concurrenten doen op dezelfde zoekopdrachten","De correcties om deze week te starten, op prioriteit","Een plan van 90 dagen, met de indicatoren die we volgen"],
 "dia_btn":"Vraag de diagnose aan","dia_label":"Wat u ontvangt",
 "brief":"Twee pagina’s van de diagnose, plat gelegd, strijklicht. Geen stockbeelden.",
 "sui_e":"Situaties","sui_t":"Vier situaties, één methode.",
 "sui_i":"U herkent de uwe. In alle vier begint het bij dezelfde diagnose, en een opdracht loopt minstens drie maanden. Dat is de tijd die de cijfers nodig hebben.",
 "cases":["U lanceert een merk en alles moet nog worden gebouwd","Uw site krijgt verkeer en levert geen aanvraag op","U bent zichtbaar op social en onvindbaar op Google","U verkoopt al en wilt de acquisitie opschalen"],
 "met_e":"Methode","met_t":"Vier fasen, in deze volgorde.",
 "stages":[("Diagnose","We kijken voordat we voorstellen. Het document blijft van u, ook als het daarbij blijft."),
           ("Plan","90 dagen, op papier, met prioriteiten, verantwoordelijken en data."),
           ("Productie","Ontwerp, tekst, ontwikkeling, advertenties. U keurt goed, wij voeren uit."),
           ("Meting","Een maandelijkse blik op de cijfers die beslissen: aanvragen, offertes, verkopen.")],
 "clo_t":"Laten we beginnen met te zien waar u staat.","clo_2":"Bekijk de diensten","clo_f":"Lissabon. Antwoord binnen twee werkdagen",
 "foot":["Diensten","Aanpak","Contact"],
 "legal":["Privacy","Cookies"],"city":"Lissabon","wa":"WhatsApp","wa_msg":"Hallo Peak Pulse, ik wil graag een diagnose aanvragen.",
}

C["ar"] = {
 "lang":"ar","dir":"rtl",
 "title":"Peak Pulse. حضور رقمي يجلب العملاء",
 "desc":"بيك بالس تبني حضوركم الرقمي وتديره. خطوة واحدة في كل مرة، بالترتيب الذي يعطي نتيجة. الرد خلال يومَي عمل.",
 "org_desc":"بيك بالس تبني حضوركم الرقمي وتديره.",
 "nav":["الخدمات","التشخيص","المنهج"],
 "cta":"اطلبوا تشخيصاً",
 "hero_t":"أن تُوجَد. ثم أن تُختار.",
 "hero_s":"بيك بالس تبني حضوركم الرقمي وتديره. الاستراتيجية، الهوية، الموقع، محركات البحث، المحتوى، الإعلان. خطوة واحدة في كل مرة، بالترتيب الذي يعطي نتيجة.",
 "hero_n":"الرد خلال يومَي عمل",
 "sit_e":"أين أنتم اليوم","sit_t":"ثلاثة أمور تكلّفكم عملاء كل أسبوع.",
 "sit":["يجدونكم، ولا أحد يفهم خلال ثلاث ثوانٍ ما الذي تبيعونه.",
        "موقعكم يستقبل زيارات لا تتحول إلى طلبات.",
        "تنشرون بانتظام دون معرفة ما يعود عليكم."],
 "mis_e":"مهمتنا","mis_t":"نبني حضوراً يغطي كلفته.",
 "mis_p1":"بيك بالس موجودة لسبب واحد. قد تكون العلامة ممتازة وتبقى غير مرئية، والعلامة غير المرئية تخسر أمام من يظهر ببساطة بشكل أفضل. هذه المسافة هي ما نغلقه.",
 "mis_p2":"نعمل على المكشوف، أولوية واحدة في كل مرة، ونربط كل خطوة برقم يهمكم أصلاً. لا ضجيج، ولا أرقام للمظهر، ولا عقود طويلة نختبئ خلفها. وحين يتوقف العمل عن أن يفيد، نقولها أولاً.",
 "prin":[("الترتيب قبل الضجيج","الفعل الصحيح في الأسبوع الصحيح. الترتيب هو معظم النتيجة."),
         ("الدليل قبل الوعد","نقيس ما ننفذه، ونعرض عليكم الأرقام التي نتابعها."),
         ("يبقى لكم","كل وثيقة، كل حساب، كل ملف يبقى باسمكم.")],
 "svc_e":"الخدمات","svc_t":"أربعة محاور، ولا نعمل عليها كلها في وقت واحد.",
 "svc_i":"نبدأ بما يعطي أثراً أسرع في حالتكم. والباقي يأتي بعد أن تثبت القاعدة.",
 "groups":[
   ("الاستراتيجية والأداء",["استراتيجية رقمية","إعلانات مدفوعة على غوغل وميتا ولينكدإن","تحليل البيانات وعائد الاستثمار","تحسين معدل التحويل"]),
   ("الظهور والمحتوى",["تحسين محركات البحث","شبكات التواصل","محتوى تحريري ونشرات وفيديو","التسويق عبر المؤثرين","السمعة الرقمية والتقييمات","العلاقات الصحفية الرقمية"]),
   ("الإبداع والتقنية",["المواقع والمتاجر الإلكترونية","هوية العلامة ودليلها","التصميم البصري","ربط أنظمة إدارة العملاء","الذكاء الاصطناعي في خدمة العلاقة مع العميل"]),
   ("النمو والولاء",["حملات البريد والأتمتة","مسار الاستقطاب","التجريب والقياس"]),
 ],
 "dia_e":"التشخيص","dia_t":"قبل أي عرض، وثيقة.",
 "dia_b":"تدقيق كامل لحضوركم الرقمي. ما ينجح، وما يعيق، وما يفعله منافسوكم، وترتيب المعالجة. الوثيقة لكم، سواء عملنا معاً أو لا.",
 "dia":["قياس دقيق لموقعكم ولظهوركم في البحث ولحساباتكم","ما يفعله منافسوكم على عمليات البحث نفسها","الإصلاحات التي تبدأ هذا الأسبوع، مرتبة حسب الأولوية","خطة 90 يوماً مع المؤشرات التي نتابعها"],
 "dia_btn":"اطلبوا التشخيص","dia_label":"ما تحصلون عليه",
 "brief":"صفحتان من التشخيص، مسطحتان، بإضاءة جانبية. لا صور من البنوك.",
 "sui_e":"الحالات","sui_t":"أربع حالات، ومنهج واحد.",
 "sui_i":"ستتعرفون على حالتكم. في الحالات الأربع تبدأ الطريق بالتشخيص نفسه، ولا تقل المهمة عن ثلاثة أشهر. هذا هو الوقت الذي تحتاجه الأرقام.",
 "cases":["تطلقون علامة جديدة وكل شيء ما زال قيد البناء","موقعكم يستقبل زواراً ولا ينتج طلبات","تظهرون على الشبكات ولا تظهرون على غوغل","تبيعون فعلاً وتريدون توسيع الاستقطاب"],
 "met_e":"المنهج","met_t":"أربع مراحل، بهذا الترتيب.",
 "stages":[("التشخيص","ننظر قبل أن نقترح. الوثيقة لكم، حتى لو توقف الأمر هنا."),
           ("الخطة","90 يوماً، مكتوبة، بالأولويات والمسؤوليات والتواريخ."),
           ("التنفيذ","تصميم، نصوص، تطوير، إعلان. توافقون، وننفذ."),
           ("القياس","مراجعة شهرية للأرقام التي تحسم: الطلبات، العروض، المبيعات.")],
 "clo_t":"لنبدأ بمعرفة أين أنتم.","clo_2":"اطّلعوا على الخدمات","clo_f":"لشبونة. الرد خلال يومَي عمل",
 "foot":["الخدمات","المنهج","التواصل"],
 "legal":["الخصوصية","ملفات الارتباط"],"city":"لشبونة","wa":"واتساب","wa_msg":"مرحباً بيك بالس، أود طلب تشخيص.",
}

# ---------------------------------------------------------------- template
def langs_html(active):
    order = [("pt","/","Português"),("en","/en/","English"),("fr","/fr/","Français"),
             ("nl","/nl/","Nederlands"),("ar","/ar/","العربية")]
    out=[]
    for code,href,title in order:
        cur = ' aria-current="true"' if code==active else ''
        d = ' dir="rtl"' if code=="ar" else ''
        out.append(f'<a href="{href}" hreflang="{code}"{cur}{d} title="{title}">{code.upper()}</a>')
    return '<div class="langs">'+''.join(out)+'</div>'

def alternates():
    out=[f'<link rel="alternate" hreflang="{c}" href="{BASE}{p}">' for c,p in PATHS.items()]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}/">')
    return '\n'.join(out)

def rail_html(d):
    items=[("situation","01",d["sit_e"]),("mission","02",d["mis_e"]),("services","03",d["svc_e"]),
           ("diagnostic","04",d["dia_e"]),("situations","05",d["sui_e"]),("method","06",d["met_e"])]
    lis=[(f'<a href="#{i}"><span class="rail-tick"></span>'
          f'<span class="rail-label">{n} {lab}</span></a>') for i,n,lab in items]
    return '<nav class="rail" aria-hidden="true">'+''.join(lis)+'</nav>'

def render(code):
    d=C[code]; rtl = d["dir"]=="rtl"; home=PATHS[code]
    WA = wa_url(d["wa_msg"])                                   # click to chat, +351 920 484 417
    WATT = f'href="{WA}" target="_blank" rel="noopener"'       # WhatsApp link attributes
    preload = ('<link rel="preload" href="/assets/fonts/naskh-400.woff2" as="font" type="font/woff2" crossorigin>\n'
               '<link rel="preload" href="/assets/fonts/bodoni-400.woff2" as="font" type="font/woff2" crossorigin>\n'
               '<link rel="preload" href="/assets/fonts/bodoni-700.woff2" as="font" type="font/woff2" crossorigin>\n'
               '<link rel="preload" href="/assets/fonts/jost-400.woff2" as="font" type="font/woff2" crossorigin>') if rtl else \
              ('<link rel="preload" href="/assets/fonts/bodoni-400.woff2" as="font" type="font/woff2" crossorigin>\n'
               '<link rel="preload" href="/assets/fonts/bodoni-700.woff2" as="font" type="font/woff2" crossorigin>\n'
               '<link rel="preload" href="/assets/fonts/jost-300.woff2" as="font" type="font/woff2" crossorigin>\n'
               '<link rel="preload" href="/assets/fonts/jost-400.woff2" as="font" type="font/woff2" crossorigin>')

    groups=''.join(
      f'<div class="group" data-reveal><h3 class="group-title">{g[0]}</h3>'
      f'<ul class="group-items">'+''.join(f'<li>{it}</li>' for it in g[1])+'</ul></div>'
      for g in d["groups"])
    stmts=''.join(f'<li class="statement" data-reveal>{s}</li>' for s in d["sit"])
    prin=''.join(f'<div class="principle" data-reveal><p class="p-kicker">{k}</p><p class="p-line">{t}</p></div>' for k,t in d["prin"])
    dlist=''.join(f'<li>{x}</li>' for x in d["dia"])
    cases=''.join(f'<li class="case" data-reveal>{c}</li>' for c in d["cases"])
    stages=''.join(
      f'<div class="stage" data-reveal><p class="stage-num">0{i+1}</p>'
      f'<h3 class="stage-name">{s[0]}</h3><p class="stage-line">{s[1]}</p></div>'
      for i,s in enumerate(d["stages"]))

    dir_attr = ' dir="rtl"' if rtl else ''
    html_tag = f'<html lang="{d["lang"]}"{dir_attr}>'
    doc = f'''<!DOCTYPE html>
{html_tag}
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d["title"]}</title>
<meta name="description" content="{d["desc"]}">
<link rel="canonical" href="{BASE}{home}">
{alternates()}
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
{preload}
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@graph":[
{{"@type":"Organization","name":"Peak Pulse","url":"{BASE}/","description":"{d['org_desc']}","areaServed":"PT","knowsLanguage":["pt","en","fr","nl","ar"]}},
{{"@type":"WebSite","name":"Peak Pulse","url":"{BASE}{home}","inLanguage":"{d['lang']}"}}]}}
</script>
</head>
<body>

<header class="site-header">
  <div class="wrap header-row">
    <a class="sig" href="{home}" aria-label="Peak Pulse">
      {wm("sig-name")}
      <span class="sig-sub">Digital Marketing Agency</span>
    </a>
    <nav class="nav" aria-label="Peak Pulse">
      <a href="#services">{d["nav"][0]}</a>
      <a href="#diagnostic">{d["nav"][1]}</a>
      <a href="#method">{d["nav"][2]}</a>
    </nav>
    <div class="header-end">
      {langs_html(code)}
      <a class="btn btn-solid header-cta" {WATT}>{d["cta"]}</a>
    </div>
  </div>
</header>

{rail_html(d)}

<main>

  <section class="hero" id="top">
    <div class="wrap">
      <h1 class="hero-title" data-reveal>{d["hero_t"]}</h1>
      <p class="hero-sub" data-reveal>{d["hero_s"]}</p>
      <div class="hero-actions" data-reveal>
        <a class="btn btn-solid" {WATT}>{d["cta"]}</a>
        <span class="hero-note">{d["hero_n"]}</span>
      </div>
    </div>
  </section>

  <div class="markband" aria-hidden="true">
    <div class="mark-rule">{SYM_MARK}<span class="mark-drop"></span></div>
    <p class="mark-word">{WMI}</p>
  </div>

  <section id="situation" data-rail>
    <div class="wrap">
      <div class="section-head">
        {eyebrow("01", d["sit_e"])}
        <h2 class="h-title" data-reveal>{d["sit_t"]}</h2>
      </div>
      <ul class="statements">{stmts}</ul>
    </div>
  </section>

  <div class="divider"></div>

  <section class="mission" id="mission" data-rail>
    <div class="wrap">
      {eyebrow("02", d["mis_e"], dark=True)}
      <h2 class="mission-title" data-reveal>{d["mis_t"]}</h2>
      <div class="mission-body">
        <p data-reveal>{d["mis_p1"]}</p>
        <p data-reveal>{d["mis_p2"]}</p>
      </div>
      <div class="principles">{prin}</div>
    </div>
  </section>

  <section id="services" data-rail>
    <div class="wrap">
      <div class="section-head">
        {eyebrow("03", d["svc_e"])}
        <h2 class="h-title" data-reveal>{d["svc_t"]}</h2>
        <p class="lead svc-intro" data-reveal>{d["svc_i"]}</p>
      </div>
      <div class="groups">{groups}</div>
    </div>
  </section>

  <div class="divider"></div>

  <section id="diagnostic" data-rail>
    <div class="wrap diag">
      <div class="diag-main">
        {eyebrow("04", d["dia_e"])}
        <h2 class="h-title" data-reveal>{d["dia_t"]}</h2>
        <p class="lead" data-reveal style="margin-top:22px">{d["dia_b"]}</p>
        <a class="btn btn-line" {WATT} data-reveal>{d["dia_btn"]}</a>
      </div>
      <div class="diag-side">
        <p class="diag-label" data-reveal>{d["dia_label"]}</p>
        <ul class="diag-list" data-reveal>{dlist}</ul>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <section id="situations" data-rail>
    <div class="wrap">
      <div class="section-head">
        {eyebrow("05", d["sui_e"])}
        <h2 class="h-title" data-reveal>{d["sui_t"]}</h2>
        <p class="lead" data-reveal style="margin-top:22px">{d["sui_i"]}</p>
      </div>
      <ul class="cases">{cases}</ul>
    </div>
  </section>

  <div class="divider"></div>

  <section id="method" data-rail>
    <div class="wrap">
      <div class="section-head">
        {eyebrow("06", d["met_e"])}
        <h2 class="h-title" data-reveal>{d["met_t"]}</h2>
      </div>
      <div class="stages">{stages}</div>
    </div>
  </section>

  <div class="divider"></div>

  <section class="closing" id="closing">
    <div class="wrap">
      <h2 class="h-title" data-reveal>{d["clo_t"]}</h2>
      <div class="closing-actions" data-reveal>
        <a class="btn btn-solid" {WATT}>{d["cta"]}</a>
        <a class="btn btn-line" href="#services">{d["clo_2"]}</a>
      </div>
      <p class="closing-fine" data-reveal>{d["clo_f"]}</p>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-sig">
        <span class="sig">{wm("sig-name")}<span class="sig-sub">Digital Marketing Agency</span></span>
      </div>
      <div class="footer-col">
        <h3>{d["foot"][0]}</h3>
        <ul>{''.join(f'<li><a href="#services">{g[0]}</a></li>' for g in d["groups"])}</ul>
      </div>
      <div class="footer-col">
        <h3>{d["foot"][1]}</h3>
        <ul>
          <li><a href="#mission">{d["mis_e"]}</a></li>
          <li><a href="#diagnostic">{d["dia_e"]}</a></li>
          <li><a href="#method">{d["met_e"]}</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>{d["foot"][2]}</h3>
        <ul>
          <li><a {WATT}>{d["cta"]}</a></li>
          <li><a {WATT}>{d["wa"]}</a></li>
          <li><span>{d["city"]}</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Peak Pulse</span>
      <span class="footer-langs">
        <a href="/"{' aria-current="true"' if code=="pt" else ''}>PT</a>
        <a href="/en/"{' aria-current="true"' if code=="en" else ''}>EN</a>
        <a href="/fr/"{' aria-current="true"' if code=="fr" else ''}>FR</a>
        <a href="/nl/"{' aria-current="true"' if code=="nl" else ''}>NL</a>
        <a href="/ar/"{' aria-current="true"' if code=="ar" else ''}>AR</a>
      </span>
      <span class="footer-legal">
        <a href="#top">{d["legal"][0]}</a>
        <a href="#top">{d["legal"][1]}</a>
      </span>
    </div>
  </div>
</footer>

<nav class="actionbar" aria-label="Peak Pulse">
  <a {WATT}>{d["cta"]}</a>
  <a {WATT}>{d["wa"]}</a>
</nav>

<script>
(function(){{
  var rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!rm){{
    var els=[].slice.call(document.querySelectorAll('[data-reveal]'));
    els.forEach(function(el){{el.classList.add('reveal');}});
    var io=new IntersectionObserver(function(list){{list.forEach(function(e){{
      if(!e.isIntersecting)return;
      var el=e.target, s=[].slice.call(el.parentNode.children).filter(function(n){{return n.hasAttribute('data-reveal');}});
      setTimeout(function(){{el.classList.add('is-in');}}, Math.max(0,s.indexOf(el))*70);
      io.unobserve(el);
    }});}},{{threshold:0.14}});
    els.forEach(function(el){{io.observe(el);}});
  }}
  var links=[].slice.call(document.querySelectorAll('.rail a'));
  var secs=[].slice.call(document.querySelectorAll('[data-rail]'));
  if(secs.length && 'IntersectionObserver' in window){{
    var so=new IntersectionObserver(function(list){{list.forEach(function(e){{
      if(!e.isIntersecting)return; var id=e.target.id;
      links.forEach(function(a){{a.classList.toggle('on', a.getAttribute('href')==='#'+id);}});
    }});}},{{rootMargin:'-45% 0px -50% 0px'}});
    secs.forEach(function(s){{so.observe(s);}});
  }}
}})();
</script>

</body>
</html>
'''
    return doc

for code in C:
    out = render(code)
    target = ROOT if code=="pt" else ROOT/code
    target.mkdir(parents=True, exist_ok=True)
    (target/"index.html").write_text(out, encoding="utf-8")
    print("wrote", (target/"index.html"), len(out.encode()), "bytes")
print("done")
