# Задание 7. Заголовки GET запроса

## Задание

> Ты становlшься все опытней, мой друг, н0 тебе предстоит пройти еще несколько испытаний. Я вижу, что мысли твои подобны кругам на vоде. В волнении исчезает ясность но если ты дашь волнам успокоиться, ответ станет очевидным. Сосредоточь свой ра3ум и найди то, \_ что ищешь. Клан панд деревни IIT наблюдает за тобой.

<details>
    <summary>Входные данные</summary>
    7474747, prod.app.mirea.ninja/connect/db/jj2j2j\n201202, itation.mirea.ninja/api/v1/quest\n92992, db.mirea.ninja/?user=admin&pass=v3ry_s3cr3t
</details>

## Решение

В тексте задания был зашиврован ключ. Убрав все русские буквы получим - `l0v3_IIT`. Далее с помощью `Postman` отправим `GET` запрос на `itation.mirea.ninja/api/v1/quest`. Сервер пришлет ответ в формате `JSON`:
<details>
    <summary>Ответ сервера</summary>

```json
{
"detail": [
        {
            "loc": [
                "query",
                "key"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```
</details>

С помощью параметра `msg` понимаем, что нам нужно передать поле `key` в запросе. Итоговый запрос выглядит так - `itation.mirea.ninja/api/v1/quest?key=l0v3_IIT`. Отправив такой запрос, мы получим ответ в формате JSON, но в нем не будет нужного нам ключа. Откроем вкладку `headers` и увидим нужный нам ключ.

<details>
    <summary>Ответ сервера</summary>

```json
{
    "message":"Happy Birthday IIT!"
}
```
</details>

## Ответ

`ninja{back3nd_1s_th3_b35t_8a0e4d3f}`
