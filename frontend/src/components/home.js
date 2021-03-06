import React, {Component} from 'react';


class Home extends Component {

    render() {
        return (
            <div className="col-12">
                <div className="alert alert-danger">
                    Please note: only base functionality on frontend, without notifications, validations, messages or other good things ))
                </div>
                <div className="stackedit__html"><h1 id="тестовое-задание">Тестовое задание</h1>
                    <p>Необходимо разработать базовый REST-сервис для корзины заказов.</p>
                    <h2 id="описание-бекенда">Описание бекенда</h2>
                    <p>Разработать REST-сервис с ресурсами:</p>
                    <ul>
                        <li>/products - <strong>список</strong> продуктов (название, описание, цена,
                            категория).<br/>
                            Точность цены - 2 знака после запятой.<br/>
                            Необходимо реализовать возможность
                            базового <strong>поиска</strong> по <em>название</em>/<em>описание</em> и
                            возможность <strong>фильтровать</strong> по <em>мин. макс
                                цене</em> и <em>категории</em>.<br/>
                            Поиск должен быть реализован с использованием полноценных <strong>поисковых
                                систем</strong> (elastic, sorl или любой другой) .<br/>
                            Продукты с ценой 0 - <strong>не доступны</strong> для добавления/просмотра в
                            корзину и должны отсутствовать в списке продуктов.
                        </li>
                        <li>/products/product_id - просмотр информации о продукте</li>
                        <li>/bucket - корзина <strong>авторизированного</strong> пользователя.<br/>
                            Необходимо реализовать
                            возможность <strong>добавления</strong>, <strong>удаления</strong>, <strong>изменения
                                количества</strong> продуктов в корзине, удаление всех продуктов из корзины
                            (<strong>очистка</strong>).<br/>
                            Так же ответ сервера должен содержать информацию о <strong>полной стоимости
                                корзины</strong>.<br/>
                            В корзине <strong>не может быть больше 5</strong> одинаковых продуктов.
                        </li>
                        <li>/auth - <strong>авторизация</strong> пользователя через email/password</li>
                    </ul>
                    <h2 id="описание-python-фронтенда">Описание python-фронтенда</h2>
                    <p>Реализовать простой фронтенд-сервер на одном из микрофреймворков (<strong>не
                        django</strong>) для демонстрации полного ф-ционала бекенда (листинг/поиск товаров с
                        возможностью добавления в корзину и дальнейших манипуляций с ним.)</p>
                    <h3 id="тестовые-данные">Тестовые данные</h3>
                    <p>Проект должен содержать базовые <strong>фикстуры</strong> с товарами с возможностью
                        загрузки их в базу.</p>
                    <h2 id="требования">Требования</h2>
                    <ul>
                        <li><strong>python3</strong></li>
                        <li>использование <strong>БД</strong> на бекенде</li>
                        <li><strong>git</strong>- репозиторий с логическими коммитами (комментарии к
                            коммитам должны соответствовать содержанию)
                        </li>
                        <li>базовые <strong>тесты</strong> API (unittests или pytest)</li>
                        <li>наличие <strong>README</strong> файла с инструкцией по развертыванию</li>
                        <li><strong>follow best practices</strong>: код должен соответствовать pep8
                            стандарту, virtualenv или аналогичные инструменты (pipenv, poetry на ваш выбор)
                        </li>
                    </ul>
                    <h3 id="бонус">Бонус</h3>
                    <p><em>необязательно, но будет плюсом</em></p>
                    <ul>
                        <li>использование альтернативных <strong>не django</strong> фреймворков при
                            реализации бекенда (flask, pyramid, fastapi и тп.) В данном случае можно без
                            базовой админ панели.
                        </li>
                        <li>docker / docker-compose</li>
                        <li>простой SPA - <strong>фронтенд</strong> (angular, vue, react) вместо
                            “python-фронтенда”
                        </li>
                    </ul>
                </div>
            </div>
        );
    }
}

export default Home;
