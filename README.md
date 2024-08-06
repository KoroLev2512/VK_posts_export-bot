# bot

***
##  С чего начать?
Для того, чтобы облегчить знакомство с сервисом GitFlic и первые шаги в нём, мы подготовили несколько рекомендаций.  
Уже опытный пользователь? Отредактируйте данный **README** файл по своему усмотрению.  
Не знаете что добавить в него? Перейдите в раздел `"Что должен содержать README файл"`, в котором описаны ключевые компоненты хорошего README файла. 

## Добавьте свои файлы
Если вы решили начать разработку проекта с создания репозитория в нашем сервисе, тогда клонируйте себе данный репозиторий следующим образом:


```
git clone https://gitflic.ru/project/zov/bot.git
cd bot
**добавьте первые файлы вашего проекта**
git add .
git commit -m "Первый коммит"
git push -u origin master
```

Уже что-то делали в проекте? В таком случае инициализируйте гит-репозиторий в корне проекта и добавьте текущий репозиторий как удалённый репозиторий:

```
cd existing_folder
git init
git remote add origin https://gitflic.ru/project/zov/bot.git
git clone
 ***добавьте новые файлы***
git add .
git commit -m "Новый коммит"
git push -u origin master
```
***


# Что должен содержать README файл


Прежде всего, стоит понимать, что `README.md` — это краткая документация. Это первое, что видит человек, который открывает репозиторий. Поэтому здесь важно дать достаточно информации о проекте и рассказать, что он из себя представляет.
Ключевая информация, которую должен содержать README файл:

## Название и описание
Название проекта должно быть простым и понятным (чаще всего это одно слово).
Описание должно описывать основные функции проекта, включая его особенности и назначение. 
Если у вашего проекта есть альтернативные проекты, то в описании можно перечислить ключевые отличия, которые выделяют ваш проект на фоне всех остальных.

## Установка и настройка
Также в `README` файле рекомендуется перечислить необходимые инструкции для установки, 
будь то использование пакетных менеджеров (например, `Homebrew` на MacOS или `apt` на Linux), 
зависимости, которые могут понадобиться в ходе использования, а также шаги по их настройке.

## Contributing
Можно добавить информацию о том, как принять участие в разработке вашего проекта, как стать непосредственным участником, правила оформления pull-requests и т.д.

## Контакты
Ссылки на внешние ресурсы, такие как документация, блог, страница проекта в социальных сетях, сообщество проекта и т.д.

## Статус проекта
В данном разделе рекомендуется указывать, на какой стадии находится проект, активно разрабатывается или находится в стадии застоя.
Если же проект готов и во всю используется, можно указывать актуальную версию, а также последние изменения, которые были сделаны с момента предыдущего релиза.

***

# Полезные ссылки

***

## Работа с проектом

- [ ] [Как создать проект](https://docs.gitflic.space/project/project_create)
- [ ] [Как импортировать проект](https://docs.gitflic.space/project/import_base)
- [ ] [Запросы на слияние](https://docs.gitflic.space/project/merge_request)
- [ ] [Зеркалирование проекта](https://docs.gitflic.space/project/mirror)
- [ ] [Импортировать проект с GitLab](https://docs.gitflic.space/project/import)

## Команды
- [ ] [Создание команды](https://docs.gitflic.space/team/create)
- [ ] [Обзор команды](https://docs.gitflic.space/team/view)
- [ ] [Настройка команды](https://docs.gitflic.space/team/settings)

## Реестр пакетов
- [ ] [Реестр пакетов](https://docs.gitflic.space/registry/package)
- [ ] [PyPi](https://docs.gitflic.space/registry/pypi_registry)
- [ ] [Generic](https://docs.gitflic.space/registry/generic_registry)
- [ ] [Maven](https://docs.gitflic.space/registry/maven_registry)
- [ ] [Docker](https://docs.gitflic.space/registry/docker)

## Компании
- [ ] [Создание компании](https://docs.gitflic.space/company/create)
- [ ] [Обзор компании](https://docs.gitflic.space/company/view)
- [ ] [Тарифы и оплата](https://docs.gitflic.space/company/price)
- [ ] [Запуск агента компании](https://docs.gitflic.space/company/saas_runner_setup)

## CI/CD
- [ ] [Что такое GitFlic CI/CD](https://docs.gitflic.space/cicd/introduction)
- [ ] [Задача (Job)](https://docs.gitflic.space/cicd/job)
- [ ] [Конвейер (pipeline)](https://docs.gitflic.space/cicd/pipeline)
- [ ] [Агенты](https://docs.gitflic.space/cicd/agent)
- [ ] [Справочник для .yaml файла](https://docs.gitflic.space/cicd/gitflic-ci-yaml)

## API
- [ ] [Введение в GitFlic API](https://docs.gitflic.space/api/intro)
- [ ] [Методы для администратора](https://docs.gitflic.space/api/admin)
- [ ] [Получение access токена](https://docs.gitflic.space/api/access-token)


## Панель администратора
- [ ] [Панель администратора](https://docs.gitflic.space/admin_panel/intro)
- [ ] [Панель управления](https://docs.gitflic.space/admin_panel/dashboard)
- [ ] [Настройка LDAP](https://docs.gitflic.space/admin_panel/ldap)
- [ ] [Ключевые настройки](https://docs.gitflic.space/admin_panel/settings)

## Общая информация
- [ ] [Глоссарий](https://docs.gitflic.space/common/gloss)
- [ ] [Права доступа ролей](https://docs.gitflic.space/common/manage_roles)
- [ ] [Вебхуки](https://docs.gitflic.space/common/webhook)