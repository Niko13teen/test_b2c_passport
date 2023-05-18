<div align="center"> <h1> Тестирование сервиса "Ростелеком ID" </h1></div>
<h4> Обьект тестирования: https://b2c.passport.rt.ru </h4>
<h4> Инструменты тестирования: Selenium WebDriver <img src="https://github.com/devicons/devicon/blob/master/icons/selenium/selenium-original.svg" title="SE" **alt="SE" width="15" height="15"/>, Pytest <img src="https://github.com/devicons/devicon/blob/master/icons/pytest/pytest-original.svg" title="pytest" **alt="pytest" width="20" height="20"/></h4>
<h4> Среда тестирования: Windows 10 <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/windows8/windows8-original.svg" title="WN" **alt="WN" width="15" height="15"/>, Google Chrome <img src="https://www.svgrepo.com/show/380996/google-chrome-logo-new.svg" title="GO" **alt="GO" width="20" height="20"/></h4>
<br>
<h4> Отчёт о результатах тестирования: </h4>
<p> Протестированы компоненты: Авторизация, Регистрация. <br>
Всего тест-кейсов: 16 <br>
Всего автоматизированных тестов: 16 <br>
Используемые техники тест-дизайна: Классы Эквивалентности, Граничные Значения.<br>
Выявлено доказанных дефектов: 0 <br>
Выявлено потенциально возможных дефектов: 3 </p>
<br>
<h4> Тестовая документация: </h4>
<p> Documentation/TestSuites.ods - наборы тест-кейсов <br>
 <p> Documentation/BugReport.ods - потенциально возможные дефекты <br>
<br>
<h4> Требования к запуску автоматизированных тестов: </h4>
<p> 1. Предустановленный Google Chrome </p>
<p> 2. Предустановленный Python не ниже версии 3.9 </p>
<p> 3. Установка зависимостей из файла requirements.txt </p>
<br>
<h4> Запуск тестов: </h4>
<pre><code> pip3 install -r requirements.txt </code>
<code> cd tests </code>
<code> pytest -v tests.py </code>
</pre>
