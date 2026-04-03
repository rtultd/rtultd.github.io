from pathlib import Path

root = Path('/mnt/data/binom-site')

services = [
    ('Автоматизация', '/services/automation.html', 'АСУ, шкафы управления, внедрение и пусконаладка'),
    ('Разработка ПО и ИС', '/services/development.html', 'Веб-системы, панели оператора, прикладное ПО и аналитика'),
    ('VR/AR', '/services/vr-ar.html', 'Интерактивные обучающие и демонстрационные решения'),
    ('Техническая документация', '/services/docs.html', 'КД, ТУ, ПМИ, эксплуатационные и ремонтные документы'),
    ('Образовательные услуги', '/services/education.html', 'Повышение квалификации и консультации под задачи заказчика'),
    ('Оснащение и испытательная база', '/services/equipment.html', 'Испытательные комплексы, измерительное и генераторное оборудование'),
]

projects = [
    ('Прессовые установки', '/projects/press-automation.html', 'Автоматизация гранулирования, миксирования и смежных процессов'),
    ('Программные проекты', '/projects/software-projects.html', 'Панели оператора, мониторинг и аналитические системы'),
    ('Работы с БПЛА', '/projects/drone-projects.html', 'Аэрофотосъемка, 3D-модели и испытательные полеты'),
]


def header(depth=''):
    service_links = '\n'.join(
        f'<a href="{depth}{href.lstrip("/")}">{title}<span>{desc}</span></a>' for title, href, desc in services
    )
    project_links = '\n'.join(
        f'<a href="{depth}{href.lstrip("/")}">{title}<span>{desc}</span></a>' for title, href, desc in projects
    )
    return f'''
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{depth}index.html">
      <span class="brand-mark" aria-hidden="true"></span>
      <span class="brand-text"><strong>Компания «РТУ»</strong><span>Проектирование, автоматизация, ПО и испытания</span></span>
    </a>
    <button class="mobile-toggle" aria-label="Открыть меню" data-mobile-toggle>☰</button>
    <nav class="nav-links" data-nav-links>
      <div class="nav-item">
        <button class="drop-toggle">Услуги</button>
        <div class="dropdown">{service_links}</div>
      </div>
      <div class="nav-item">
        <button class="drop-toggle">Наши проекты</button>
        <div class="dropdown">{project_links}</div>
      </div>
      <a class="nav-link" href="{depth}about.html">О компании</a>
      <a class="nav-link" href="{depth}team.html">Команда</a>
      <a class="nav-link" href="{depth}contacts.html">Контакты</a>
      <a class="cta-small" href="{depth}contacts.html#request">Заказать проект</a>
    </nav>
  </div>
</header>
'''


def footer(depth=''):
    return f'''
<footer class="site-footer">
  <div class="container footer-inner">
    <div>© <span data-year></span> Компания «РТУ»</div>
    <div class="footer-links">
      <a href="{depth}index.html">Главная</a>
      <a href="{depth}about.html">О компании</a>
      <a href="{depth}team.html">Команда</a>
      <a href="{depth}contacts.html">Контакты</a>
      <a href="{depth}privacy.html">Политика конфиденциальности</a>
    </div>
  </div>
</footer>
<script src="{depth}assets/js/main.js"></script>
'''


def page(title, desc, body, depth=''):
    return f'''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{depth}assets/css/styles.css">
</head>
<body>
{header(depth)}
{body}
{footer(depth)}
</body>
</html>'''


def hero_page(title, text):
    return f'''
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Технологические решения для заказчиков</div>
    <h1>{title}</h1>
    <p>{text}</p>
  </div>
</section>
'''

index_body = f'''
<section class="hero">
  <div class="container hero-content">
    <div>
      <div class="eyebrow">Проектирование, автоматизация и инженерные технологии</div>
      <h1>Разрабатываем инженерные решения, программные продукты и испытательные комплексы для промышленности и науки</h1>
      <p>Компания «РТУ» помогает заказчикам пройти путь от идеи и технического задания до опытного образца, программного продукта, автоматизированной установки и комплекта документации для внедрения.</p>
      <div class="hero-actions">
        <a class="btn" href="contacts.html#request">Заказать разработку</a>
        <a class="btn-secondary" href="about.html">Узнать о центре</a>
      </div>
    </div>
    <div class="hero-panel reveal">
      <div class="metrics">
        <div class="metric"><strong>10+</strong><span>направлений работ: от микроэлектроники и СВЧ до БПЛА, ПО и VR/AR</span></div>
        <div class="metric"><strong>3</strong><span>ключевых формата взаимодействия: разработка, оснащение, сопровождение</span></div>
        <div class="metric"><strong>Full-cycle</strong><span>ведем проекты от анализа задачи до внедрения и передачи документации</span></div>
        <div class="metric"><strong>B2B</strong><span>ориентируемся на предприятия, лаборатории, вузы и технологические команды</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="eyebrow">Что мы делаем</div>
    <h2 class="section-title">Услуги компании</h2>
    <p class="lead">Сайт собран как аккуратная презентационная площадка для заказчиков. Основные услуги вынесены в отдельные страницы, а важные проекты доступны из выпадающего меню в шапке.</p>
    <div class="grid-3" style="margin-top:32px;">
      <a class="card reveal" href="services/automation.html"><div class="icon-box">⚙️</div><h3>Автоматизация процессов</h3><p>Проектирование шкафов управления, разработка алгоритмов и программирование контроллеров и панелей оператора.</p><span class="link-arrow">Открыть страницу →</span></a>
      <a class="card reveal" href="services/development.html"><div class="icon-box">💻</div><h3>Разработка ПО и информационных систем</h3><p>Веб-сервисы, интерфейсы операторов, аналитические панели и специализированные прикладные решения.</p><span class="link-arrow">Открыть страницу →</span></a>
      <a class="card reveal" href="services/docs.html"><div class="icon-box">📘</div><h3>Техническая документация</h3><p>Подготовка конструкторских и эксплуатационных документов, описаний алгоритмов и материалов для передачи заказчику.</p><span class="link-arrow">Открыть страницу →</span></a>
      <a class="card reveal" href="services/education.html"><div class="icon-box">🎓</div><h3>Консультационные и образовательные услуги</h3><p>Программы повышения квалификации, прикладные курсы и экспертное сопровождение проектных команд.</p><span class="link-arrow">Открыть страницу →</span></a>
      <a class="card reveal" href="services/vr-ar.html"><div class="icon-box">🧩</div><h3>VR и AR решения</h3><p>Интерактивные тренажеры, демонстрации, обучающие приложения и цифровые презентации сложных процессов.</p><span class="link-arrow">Открыть страницу →</span></a>
      <a class="card reveal" href="services/equipment.html"><div class="icon-box">🛰️</div><h3>Оснащение и испытательная база</h3><p>Измерительные комплексы, генераторы, СВЧ-оборудование и инфраструктура для испытаний и отработки изделий.</p><span class="link-arrow">Открыть страницу →</span></a>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container stats-band reveal">
    <div class="grid-4">
      <div><strong>ПО</strong><span>панели управления, мониторинг, аналитика и прикладные информационные системы</span></div>
      <div><strong>АСУ</strong><span>автоматизация технологических установок и подготовка к внедрению</span></div>
      <div><strong>БПЛА</strong><span>аэрофотосъемка, испытательные работы и инженерные задачи</span></div>
      <div><strong>Документация</strong><span>сопровождение проекта полным комплектом материалов для заказчика</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <div class="eyebrow">Почему такой сайт удобно использовать</div>
      <h2 class="section-title">Понятная структура для заказчика</h2>
      <p class="lead">Главная страница быстро объясняет, чем занимается центр. Дальше посетитель может раскрыть меню услуг или проектов, перейти на нужную страницу, прочитать подробнее о направлениях и сразу оставить заявку через форму на странице контактов.</p>
      <ul class="check-list">
        <li>единый хедер и футер на всем сайте;</li>
        <li>раскрывающиеся меню с логичной группировкой страниц;</li>
        <li>современная, но спокойная анимация без перегруженности;</li>
        <li>подготовка под публикацию на GitHub Pages без сложной сборки.</li>
      </ul>
    </div>
    <div class="visual reveal">
      <div class="visual-lines"></div>
      <div class="visual-label">GitHub Pages ready</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="eyebrow">Реализованные направления</div>
    <h2 class="section-title">Наши проекты</h2>
    <div class="grid-3" style="margin-top:30px;">
      <a class="card reveal" href="projects/press-automation.html"><h3>Автоматизация прессовых установок</h3><p>Комплексные решения для гранулирования, миксирования и смежных технологических операций с использованием контроллеров, датчиков и панелей визуализации.</p><span class="link-arrow">Смотреть проект →</span></a>
      <a class="card reveal" href="projects/software-projects.html"><h3>Программные проекты</h3><p>Интерфейсы управления оборудованием, программные панели мониторинга, системы визуализации и сервисы обработки данных.</p><span class="link-arrow">Смотреть проект →</span></a>
      <a class="card reveal" href="projects/drone-projects.html"><h3>Работа с применением БПЛА</h3><p>Аэрофотосъемка, ортофотопланы, 3D-модели, испытательные полеты и инженерные обследования объектов.</p><span class="link-arrow">Смотреть проект →</span></a>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container cta-panel reveal">
    <div>
      <h2 style="margin:0 0 12px; font-size: clamp(30px,4vw,46px); letter-spacing:-.03em;">Есть задача для разработки?</h2>
      <p>Подготовили отдельную страницу контактов с формой заявки, быстрыми способами связи и ссылкой на политику конфиденциальности. Ее можно использовать как финальную точку всех продающих сценариев сайта.</p>
    </div>
    <div>
      <a class="btn" href="contacts.html#request">Оставить заявку</a>
    </div>
  </div>
</section>
'''

about_body = hero_page('О компании', 'Мы выполняем исследования и разработки в области радиоэлектронной аппаратуры, микроэлектроники, программного обеспечения, автоматизации и испытательных технологий для систем различного назначения.') + '''
<section class="section">
  <div class="container split">
    <div class="reveal">
      <h2 class="section-title">Чем полезен центр заказчику</h2>
      <p class="lead">Дизайн-центр выступает как инженерная команда полного цикла. Мы можем подключиться на раннем этапе, помочь сформировать техническое задание, подготовить архитектуру решения, выполнить разработку, испытания и сопровождение при внедрении.</p>
      <ul class="bullet-list">
        <li>поиск и проработка технических решений под прикладную задачу;</li>
        <li>разработка аппаратной части, встроенного и прикладного ПО;</li>
        <li>создание опытных образцов и стендов для испытаний;</li>
        <li>подготовка документации для передачи результата заказчику;</li>
        <li>обучение персонала и консультационное сопровождение.</li>
      </ul>
    </div>
    <div class="contact-box reveal">
      <h3 style="margin-top:0;">Основной фокус</h3>
      <p>Мы ориентируемся на прикладные инженерные задачи, где требуется совместить электронику, программирование, автоматизацию, измерения и аккуратную проектную упаковку результата.</p>
      <div class="notice">Сайт можно легко дополнять новыми направлениями, кейсами, сотрудниками, публикациями и новостями без изменения общей структуры.</div>
    </div>
  </div>
</section>
<section class="section-tight">
  <div class="container stats-band reveal">
    <div class="grid-4">
      <div><strong>Исследования</strong><span>анализ задач и выбор оптимальной технической концепции</span></div>
      <div><strong>Разработка</strong><span>аппаратные и программные компоненты для опытных и серийных решений</span></div>
      <div><strong>Испытания</strong><span>проверка работоспособности и отработка режимов эксплуатации</span></div>
      <div><strong>Передача</strong><span>документация, обучение, внедрение и сопровождение</span></div>
    </div>
  </div>
</section>
'''

team_body = hero_page('Команда компании', 'На странице собрана базовая презентация ключевых специалистов. Карточки легко редактируются, поэтому позже сюда можно добавить реальные фото, должности, публикации и направления экспертизы.') + '''
<section class="section">
  <div class="container grid-4">
    <div class="card team-card reveal"><div class="avatar">СГ</div><h3>Сергей Гагинин</h3><div class="role">Директор</div></div>
    <div class="card team-card reveal"><div class="avatar">АИ</div><h3>Алексей Исаенко</h3><div class="role">Инженер</div></div>
    <div class="card team-card reveal"><div class="avatar">АН</div><h3>Александр Нечаев</h3><div class="role">Заместитель директора</div></div>
    <div class="card team-card reveal"><div class="avatar">ПШ</div><h3>Глеб Шмырин</h3><div class="role">Инженер-электроник</div></div>
    <div class="card team-card reveal"><div class="avatar">АБ</div><h3>Артём Бражников</h3><div class="role">Инженер-программист</div></div>
    <div class="card team-card reveal"><div class="avatar">ЯС</div><h3>Ярослав Скиданов</h3><div class="role">Программист</div></div>
    <div class="card team-card reveal"><div class="avatar">АШ</div><h3>Алексей Шангин</h3><div class="role">Специалист по испытаниям</div></div>
    <div class="card team-card reveal"><div class="avatar">АК</div><h3>Алексей Константинов</h3><div class="role">Проектный менеджер</div></div>
    <div class="card team-card reveal"><div class="avatar">Ан</div><h3>Анжела Акопян</h3><div class="role">Системный аналитик</div></div>
    <div class="card team-card reveal"><div class="avatar">ВК</div><h3>Виктория Киященко</h3><div class="role">Web-разработка</div></div>
    <div class="card team-card reveal"><div class="avatar">МТ</div><h3>Максим Теняков</h3><div class="role">Инженер</div></div>
  </div>
</section>
'''

contacts_body = hero_page('Контакты', 'Если вам нужен опытный образец, автоматизация, программный продукт, учебный курс или инженерная консультация, свяжитесь с нами любым удобным способом.') + '''
<section class="section">
  <div class="container split">
    <div class="contact-box reveal">
      <h2 class="section-title" style="font-size:34px;">Связаться с нами</h2>
      <div class="contact-list">
        <a href="tel:+79277229081"><strong>Телефон:</strong>&nbsp;+7 927 722 90 81</a>
        <a href="mailto:rtultd@yandex.ru"><strong>Email:</strong>&nbsp;rtultd@yandex.ru</a>
        <div><strong>Адрес:</strong>&nbsp;г. Самара, ул. Первомайская, д. 1</div>
        <div><strong>Режим связи:</strong>&nbsp;по будням, по предварительной договоренности</div>
      </div>
    </div>
    <div class="map-card reveal"><span class="map-pin"></span></div>
  </div>
</section>
<section class="section-tight" id="request">
  <div class="container contact-box reveal">
    <div class="eyebrow">Форма заявки</div>
    <h2 class="section-title" style="font-size:40px;">Заказать разработку</h2>
    <p class="lead">Форма сделана как демонстрационная часть сайта для GitHub Pages. Для отправки реальных заявок позже можно подключить Formspree, Netlify Forms, собственный серверный обработчик или Telegram-бота.</p>
    <form class="form-grid" onsubmit="event.preventDefault(); alert('Демонстрационная форма. Для публикации можно подключить реальный обработчик заявок.');">
      <input class="input" type="email" placeholder="Email" required>
      <input class="input" type="text" placeholder="Имя" required>
      <input class="input" type="tel" placeholder="Телефон">
      <textarea class="input" placeholder="Описание заказа или вопроса"></textarea>
      <button class="btn" type="submit" style="border:none; cursor:pointer; width:max-content;">Отправить заявку</button>
    </form>
    <p class="form-note">Нажимая на кнопку, пользователь подтверждает согласие на обработку персональных данных и принимает условия, описанные в <a href="privacy.html" style="color:var(--primary);">политике конфиденциальности</a>.</p>
  </div>
</section>
'''

privacy_body = hero_page('Политика конфиденциальности', 'Страница подготовлена как базовый шаблон политики для корпоративного сайта. Перед запуском лучше проверить текст у юриста и скорректировать под фактический порядок обработки персональных данных.') + '''
<section class="section">
  <div class="container contact-box reveal">
    <h2 style="margin-top:0;">1. Общие положения</h2>
    <p class="lead" style="max-width:none;">Настоящая политика описывает порядок обработки персональных данных пользователей сайта Компании «РТУ». Оператор принимает необходимые организационные и технические меры для защиты информации от неправомерного доступа, изменения, раскрытия или уничтожения.</p>
    <h2>2. Какие данные могут обрабатываться</h2>
    <ul class="bullet-list">
      <li>имя пользователя, номер телефона и адрес электронной почты;</li>
      <li>сведения, добровольно указанные в сообщении через форму обратной связи;</li>
      <li>технические данные, которые автоматически передаются браузером при открытии страниц сайта.</li>
    </ul>
    <h2>3. Цели обработки</h2>
    <ul class="bullet-list">
      <li>обратная связь с пользователем;</li>
      <li>подготовка коммерческих предложений и консультаций;</li>
      <li>улучшение работы сайта и анализ пользовательских сценариев.</li>
    </ul>
    <h2>4. Права пользователя</h2>
    <p class="lead" style="max-width:none;">Пользователь вправе запросить уточнение, блокирование или удаление своих персональных данных, а также получить сведения об их обработке. Для этого можно направить обращение на контактный адрес электронной почты, указанный на сайте.</p>
    <h2>5. Контакты оператора</h2>
    <p class="lead" style="max-width:none;">По вопросам обработки персональных данных можно обратиться по адресу: <a href="mailto:rtultd@yandex.ru" style="color:var(--primary);">rtultd@yandex.ru</a>.</p>
  </div>
</section>
'''

service_pages = {
    'services/automation.html': (
        'Автоматизация процессов',
        'АСУ, шкафы управления и пусконаладочные решения для технологических установок.',
        hero_page('Автоматизация прессовых установок', 'Разрабатываем системы автоматического управления, которые помогают стабилизировать технологический процесс, снизить влияние человеческого фактора и обеспечить повторяемость результата.') + '''
<section class="section">
  <div class="container grid-2">
    <div class="card reveal"><h3>Система автоматического управления прессованием</h3><p>Проект включает проектирование архитектуры управления, подбор элементов, разработку программного обеспечения и интерфейсов оператора, а также настройку режимов и диагностики аварийных состояний.</p></div>
    <div class="card reveal"><h3>Что получает заказчик</h3><p>На выходе заказчик получает согласованную логику работы установки, понятный интерфейс, комплект документов и основу для дальнейшего масштабирования или модернизации оборудования.</p></div>
    <div class="card reveal"><h3>Система автоматического гранулирования</h3><p>Решение позволяет управлять последовательностью операций, выдерживать временные параметры, контролировать сигналы датчиков и обеспечивать повторяемость качества продукции.</p></div>
    <div class="card reveal"><h3>Смежные процессы</h3><p>В ту же структуру сайта можно включать страницы по миксированию, дозированию, термостатированию, упаковке и другим технологическим участкам предприятия.</p></div>
  </div>
</section>
<section class="section-tight"><div class="container split"><div class="visual reveal"><div class="visual-lines"></div><div class="visual-label">PLC / HMI / SCADA</div></div><div class="reveal"><h2 class="section-title">Подход к проекту</h2><ul class="check-list"><li>обследование действующего процесса и формирование требований;</li><li>разработка схем и алгоритмов работы оборудования;</li><li>программирование, тестирование и пусконаладка;</li><li>подготовка материалов для эксплуатационного персонала.</li></ul></div></div></section>'''
    ),
    'services/development.html': (
        'Разработка ПО и информационных систем',
        'Веб-системы, интерфейсы операторов и прикладные цифровые решения.',
        hero_page('Разработка ПО и информационных систем', 'Предлагаем широкий спектр услуг по созданию прикладных программных решений: от интерфейсов операторов и панелей мониторинга до полноценных информационных систем с аналитикой и хранением данных.') + '''
<section class="section"><div class="container grid-2"><div class="card reveal"><div class="icon-box">🖥️</div><h3>Разработка ПО</h3><p>Проектируем интерфейсы, сервисы обработки данных, инструменты мониторинга и специализированные приложения под конкретную отраслевую задачу.</p></div><div class="card reveal"><div class="icon-box">📊</div><h3>Информационные системы</h3><p>Создаем системы с аналитическими модулями и визуализацией, которые позволяют принимать решения на основе оперативных данных и накопленной статистики.</p></div></div></section>
<section class="section-tight"><div class="container contact-box reveal"><h2 style="margin-top:0;">Что можно показывать на странице</h2><ul class="bullet-list"><li>скриншоты интерфейсов и панелей управления;</li><li>описание функций системы и бизнес-эффекта для заказчика;</li><li>интеграции с БД, оборудованием и внешними сервисами;</li><li>кейсы из промышленности, образования, медицины и научных проектов.</li></ul></div></section>'''
    ),
    'services/vr-ar.html': (
        'VR и AR решения',
        'Виртуальная и дополненная реальность для обучения, демонстрации и моделирования.',
        hero_page('Виртуальная и дополненная реальность', 'Создаем прикладные VR и AR решения для обучения, инженерной визуализации, презентаций и интерактивного сопровождения сложных технических продуктов.') + '''
<section class="section"><div class="container grid-2"><div class="card reveal"><h3>VR-приложения</h3><p>Учебные тренажеры, демонстрационные среды и интерактивные сценарии, которые помогают безопасно отрабатывать действия и показывать сложные процессы наглядно.</p></div><div class="card reveal"><h3>AR-приложения</h3><p>Дополнение реальных объектов цифровыми слоями, инструкциями, подсказками и 3D-моделями для сопровождения работ и презентации решений.</p></div><div class="card reveal"><h3>Виртуальные туры и презентации</h3><p>Форматы для выставок, переговоров, привлечения партнеров и демонстрации возможностей центра без перегрузки текстом.</p></div><div class="card reveal"><h3>Обучение и симуляции</h3><p>Подготовка образовательных сценариев для вузов, предприятий и технологических команд с учетом целевой аудитории и уровня сложности материала.</p></div></div></section>'''
    ),
    'services/docs.html': (
        'Разработка технической документации',
        'Подготовка конструкторских, программных и эксплуатационных документов.',
        hero_page('Разработка технической документации', 'Техническая документация делает инженерный результат воспроизводимым, проверяемым и готовым к внедрению. Мы помогаем оформить проект так, чтобы им можно было пользоваться на производстве и в эксплуатации.') + '''
<section class="section"><div class="container contact-box reveal"><h2 style="margin-top:0;">Мы можем подготовить</h2><div class="grid-2"><div><ul class="bullet-list"><li>конструкторские документы;</li><li>технические описания и руководства;</li><li>технические условия и методики испытаний;</li><li>эксплуатационные и ремонтные документы.</li></ul></div><div><ul class="bullet-list"><li>программные документы;</li><li>описания алгоритмов и структур данных;</li><li>комплекты материалов для передачи заказчику;</li><li>поддержку приведения документов к внутренним стандартам организации.</li></ul></div></div></div></section>'''
    ),
    'services/education.html': (
        'Консультационные и образовательные услуги',
        'Курсы, экспертное сопровождение и программы повышения квалификации.',
        hero_page('Консультационные и образовательные услуги', 'Оказываем консультационные и образовательные услуги в области автоматизации, разработки электроники, микроэлектроники и программного обеспечения. Формат можно настроить под цели предприятия или учебной группы.') + '''
<section class="section"><div class="container split"><div class="reveal"><h2 class="section-title">Форматы работы</h2><ul class="check-list"><li>короткие прикладные консультации по постановке задачи;</li><li>программы повышения квалификации;</li><li>корпоративные курсы под нужды предприятия;</li><li>сопровождение студенческих и инженерных команд.</li></ul></div><div class="contact-box reveal"><p>По завершении курса можно предусмотреть выдачу документов установленного образца, а сам сайт можно дополнить отдельной страницей с перечнем программ, темами занятий и форматом записи.</p></div></div></section>'''
    ),
    'services/equipment.html': (
        'Оснащение и испытательная база',
        'Испытательная база, генераторы, анализаторы и измерительные комплексы.',
        hero_page('Оснащение и испытательная база', 'Центр располагает испытательной и измерительной базой, которая позволяет проводить анализ, отладку, проверку работоспособности и демонстрацию инженерных решений заказчикам и партнерам.') + '''
<section class="section"><div class="container grid-2"><div class="card reveal"><h3>Комплекс генерации СВЧ сигналов</h3><p>Используется для формирования, анализа и тестирования сигналов в широком диапазоне частот, а также для исследовательских и учебных задач.</p></div><div class="card reveal"><h3>Комплекс анализа спектра и сигналов</h3><p>Подходит для контроля параметров, диагностики и сопровождения разработки радиоэлектронных устройств.</p></div><div class="card reveal"><h3>Комплекс генерации широкополосных сигналов</h3><p>Используется для моделирования условий работы систем связи и навигации, испытаний и стендовой отработки.</p></div><div class="card reveal"><h3>Комплексы измерения временных параметров</h3><p>Нужны для настройки, проверки и протоколирования параметров в рамках прикладных исследований и разработки аппаратуры.</p></div></div></section>'''
    ),
}

project_pages = {
    'projects/press-automation.html': (
        'Автоматизация прессовых установок — проекты',
        'Кейсы по автоматизации гранулирования, миксирования и смежных процессов.',
        hero_page('Автоматизация прессовых установок', 'Страница проекта показывает, как можно оформить практический кейс: описать задачу, внедренное решение, этапы выполнения и ожидаемый эффект для заказчика.') + '''
<section class="section"><div class="container timeline reveal"><div class="timeline-item" data-step="1"><h4>Анализ технологического процесса</h4><p>Сбор исходных данных, изучение режимов работы оборудования, ограничений и критериев качества результата.</p></div><div class="timeline-item" data-step="2"><h4>Проектирование логики управления</h4><p>Подготовка архитектуры, выбор сигналов, сценариев работы, блокировок и аварийной логики.</p></div><div class="timeline-item" data-step="3"><h4>Разработка интерфейсов оператора</h4><p>Создание понятных экранов управления, диагностики и визуализации состояния установки.</p></div><div class="timeline-item" data-step="4"><h4>Отладка и внедрение</h4><p>Проверка алгоритмов, настройка режимов, демонстрация заказчику и сопровождение запуска.</p></div></div></section>'''
    ),
    'projects/software-projects.html': (
        'Программные проекты',
        'Примеры цифровых решений, панелей оператора и аналитических интерфейсов.',
        hero_page('Программное обеспечение', 'Здесь собраны примеры программных продуктов: от интерфейсов управления оборудованием и панелей мониторинга до аналитических систем для оценки параметров и поддержки принятия решений.') + '''
<section class="section"><div class="container grid-2"><div class="card reveal"><h3>ПО для автоматизации гранулирования</h3><p>Приложение для управления узлами установки, отображения параметров, обработки сигналов и фиксации состояния оборудования.</p></div><div class="card reveal"><h3>ПО для автоматизации миксирования</h3><p>Система управления последовательностью операций, контролем датчиков и визуализацией процесса с сохранением параметров.</p></div><div class="card reveal"><h3>ПО для оценки параметров рынка труда</h3><p>Пример веб-решения с аналитическими блоками, графиками и механизмами ранжирования данных под прикладную задачу.</p></div><div class="card reveal"><h3>ПО для оценки состояния специалистов</h3><p>Многопользовательское приложение с разграничением прав доступа, формами ввода данных и модулем отчетности.</p></div></div></section>'''
    ),
    'projects/drone-projects.html': (
        'Проекты с применением БПЛА',
        'Аэрофотосъемка, 3D-моделирование и испытательные работы.',
        hero_page('Работа с применением БПЛА', 'Беспилотные авиационные системы могут использоваться для инженерных обследований, аэрофотосъемки, испытаний изделий и подготовки пространственных данных.') + '''
<section class="section"><div class="container split"><div class="contact-box reveal"><h2 style="margin-top:0;">Выполняемые виды работ</h2><div class="timeline"><div class="timeline-item" data-step="1"><h4>Аэрофотосъемка</h4><p>Получение исходных материалов для анализа объектов и территории.</p></div><div class="timeline-item" data-step="2"><h4>Ортофотопланы и 3D-модели</h4><p>Подготовка цифровых моделей местности и объектов для визуализации и измерений.</p></div><div class="timeline-item" data-step="3"><h4>Испытания изделий специального назначения</h4><p>Проверка сценариев работы и сбор экспериментальных данных.</p></div><div class="timeline-item" data-step="4"><h4>Консультации по эксплуатации БАС</h4><p>Методическая и практическая помощь командам заказчика.</p></div></div></div><div class="visual reveal"><div class="visual-lines"></div><div class="visual-label">UAV / Mapping / Inspection</div></div></div></section>'''
    )
}

pages = {
    'index.html': ('Компания «РТУ»', 'Сайт Компании «РТУ»: услуги, проекты, контакты и инженерные компетенции.', index_body),
    'about.html': ('О компании', 'О компании, направления работ и формат взаимодействия с заказчиками.', about_body),
    'team.html': ('Команда компании', 'Ключевые специалисты и структура команды.', team_body),
    'contacts.html': ('Контакты', 'Контакты, форма заявки и способы связи.', contacts_body),
    'privacy.html': ('Политика конфиденциальности', 'Политика конфиденциальности сайта.', privacy_body),
}

for path, (title, desc, body) in pages.items():
    (root / path).write_text(page(title, desc, body), encoding='utf-8')

for path, (title, desc, body) in service_pages.items():
    (root / path).write_text(page(title, desc, body, depth='../'), encoding='utf-8')

for path, (title, desc, body) in project_pages.items():
    (root / path).write_text(page(title, desc, body, depth='../'), encoding='utf-8')

(root / 'README.md').write_text('''# Сайт Компании «РТУ»

Статический многостраничный сайт, подготовленный для публикации на GitHub Pages.

## Что внутри

- `index.html` — главная страница
- `about.html` — о центре
- `team.html` — команда
- `contacts.html` — контакты и форма заявки
- `privacy.html` — политика конфиденциальности
- `services/` — страницы услуг
- `projects/` — страницы проектов
- `assets/css/styles.css` — общие стили
- `assets/js/main.js` — раскрывающееся меню, мобильная навигация и анимация появления блоков

## Как опубликовать на GitHub Pages

1. Создайте новый репозиторий на GitHub.
2. Загрузите в него содержимое этой папки.
3. В настройках репозитория откройте раздел **Pages**.
4. Выберите публикацию из ветки `main` и корневой папки `/root`.
5. Сохраните настройки. Через несколько минут сайт станет доступен по ссылке GitHub Pages.

## Что можно улучшить после публикации

- подключить реальные фотографии и изображения проектов;
- добавить обработчик формы обратной связи;
- разместить SEO-метатеги и фавикон;
- добавить новости, публикации и кейсы.
''', encoding='utf-8')
