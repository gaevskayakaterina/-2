import numpy as np
import pandas as pd

"""
Выполнила: Гаевская
1.1 В файлах `recipes_sample.csv` и `reviews_sample.csv` 
находится информация об рецептах блюд и отзывах на эти рецепты 
соответственно. Загрузите данные из файлов в виде `pd.DataFrame` 
с названиями `recipes` и `reviews`. Обратите внимание на корректное 
считывание столбца с индексами в таблице `reviews` (безымянный столбец).
"""
recipes_df = pd.read_csv("../../data/recipes_sample.csv", parse_dates=['submitted'], delimiter=',')
reviews_df = pd.read_csv("../../data/reviews_sample.csv", index_col=0, delimiter=',')
print('1.1 Загрузите данные из файлов в виде `pd.DataFrame` с названиями `recipes` и `reviews`')
print('датафрейм рецептов:\n', recipes_df)
print('_' * 100)
print('датафрейм отзывов:\n', reviews_df)
print('_' * 100)

"""
Выполнила: Гаевская
1.2 Для каждой из таблиц выведите основные параметры:
* количество точек данных (строк);
* количество столбцов;
* тип данных каждого столбца.
"""
print('1.2 Для каждой из таблиц выведите основные параметры')
print('количество строк в датафрейме с рецептами равно', len(recipes_df.index))
print('количество строк в датафрейме с отзывами равно ', len(reviews_df.index))

print('число столбцов в датафрейме с рецептами равно ', len(recipes_df.axes[1]))
print('число столбцов в датафрейме с отзывами равно ', len(reviews_df.axes[1]))
print('_' * 100)
print('типы данных в датафрейме с рецептами:\n', recipes_df.dtypes)
print('_' * 100)
print('типы данных в датафрейме с отзывами: \n', reviews_df.dtypes)
print('_' * 100)

"""
Выполнила: Гаевская
1.3 Исследуйте, в каких столбцах таблиц содержатся пропуски. Посчитайте 
долю строк, содержащих пропуски, в отношении к общему количеству строк.
"""
print('1.3 Исследуйте, в каких столбцах таблиц содержатся пропуски')
print('количество пропусков в столбцах датафрейма с рецептами:\n', recipes_df.isnull().sum(axis=0))
print('_' * 100)
print('количество пропусков в столбцах датафрейма с отзывами:\n', reviews_df.isnull().sum(axis=0))
print('_' * 100)
print('Доля строк с пропусками в датафрейме с рецептами:\n', (recipes_df.isnull().sum(axis=0) / len(recipes_df)))
print('_' * 100)
print('Доля строк с пропусками в датафрейме с отзывами:\n', (reviews_df.isnull().sum(axis=0) / len(reviews_df)))
print('_' * 100)

"""
Выполнила: Гаевская
1.4 Рассчитайте среднее значение для каждого из числовых столбцов (где это имеет смысл).
"""
print('1.4 Рассчитайте среднее значение для каждого из числовых столбцов')
print('среднее значение для столбцов в датафрейме с рецептами:\n', recipes_df.mean(axis=0, numeric_only=True))
print('среднее значение для столбцов в датафрейме с отзывами:\n', reviews_df.mean(axis=0, numeric_only=True))
print('_' * 100)

"""
Выполнила: Гаевская
1.5 Создайте серию из 10 случайных названий рецептов.
"""
print('1.5 Создайте серию из 10 случайных названий рецептов.')
dataframe_for_task5 = recipes_df[['name']]
print('десять случайных рецептов:\n', dataframe_for_task5.sample(n=10))
print('_' * 100)

"""
Выполнила: Гаевская
1.6 Измените индекс в таблице `reviews`, пронумеровав строки, начиная с нуля.
"""
print('1.6 Измените индекс в таблице `reviews`, пронумеровав строки, начиная с нуля')
print('датафрейм отзывов с измененными индексами:\n', reviews_df.reset_index(drop=True))
print('_' * 100)

"""
Выполнила: Гаевская
1.7 Выведите информацию о рецептах, время выполнения которых 
не больше 20 минут и кол-во ингредиентов в которых не больше 5.
"""
print('1.7 Выведите информацию о рецептах, время выполнения которых не больше 20 минут и кол-во ингредиентов в которых не больше 5')
print('рецепты не дольше 20 минут и нев больше,чем из 5 ингридиентов:\n', recipes_df[(recipes_df['minutes'] <= 20) & (recipes_df['n_ingredients'] <= 5)])
print('_' * 100)

"""
Выполнила: Матвейчук
2.1 Преобразуйте столбец `submitted` из таблицы `recipes` в формат времени. 
Модифицируйте решение задачи 1.1 так, чтобы считать столбец сразу в нужном формате.
"""
print('2.1 Преобразуйте столбец `submitted` из таблицы `recipes` в формат времени')
recipes_df = pd.read_csv("../../data/recipes_sample.csv", parse_dates=['submitted'])
recipes_df['submitted'] = pd.to_datetime(recipes_df['submitted'])
print('Выполнено', '_' * 100)

"""
Выполнила: Матвейчук
2.2 Выведите информацию о рецептах, добавленных в датасет не позже 2010 года.
"""
print('2.2 Выведите информацию о рецептах, добавленных в датасет не позже 2010 года')
mask = (recipes_df['submitted'] < '2010-01-01')
print(recipes_df.loc[mask])
print('_' * 100)

"""
Выполнила: Гаевская
3.1 Добавьте в таблицу recipes столбец description_length, 
в котором хранится длина описания рецепта из столбца description.
"""
print('3.1 Добавьте в таблицу recipes столбец description_length')
recipes_df['description_length'] = recipes_df['description'].fillna('').str.len()
print('Выполнено', '_' * 100)

""" 
Выполнила: Матвейчук
3.2 Измените название каждого рецепта в таблице recipes таким 
образом, чтобы каждое слово в названии начиналось с прописной буквы.
"""
print('3.2 Измените название каждого рецепта в таблице recipes')
recipes_df['name'] = recipes_df['name'].str.capitalize()
print('Выполнено', '_' * 100)

"""
Выполнила: Матвейчук
3.3 Добавьте в таблицу recipes столбец name_word_count, в котором 
хранится количество слов из названии рецепта (считайте, что слова 
в названии разделяются только пробелами). Обратите внимание, что 
между словами может располагаться несколько пробелов подряд.
"""
print('3.3 Добавьте в таблицу recipes столбец name_word_count, в котором хранится количество слов из названии рецепта')
recipes_df['name_word_count'] = recipes_df['name'].fillna('').str.replace('  ', ' ').str.split(' ').str.len()
print('Выполнено', '_' * 100)

"""
Выполнила: Матвейчук
4.1 Посчитайте количество рецептов, представленных каждым из участников 
(`contributor_id`). Какой участник добавил максимальное кол-во рецептов?
"""
recipes = pd.read_csv('../../data/recipes_sample.csv', delimiter=',')
print('4.1 Посчитайте количество рецептов')
print('\nid участника и количество его рецептов: \n', recipes['contributor_id'].value_counts())
print('\nучастник, добавивший максимальное кол-во рецептов; макс. кол-во рецептов: ')
max_recipes = recipes['contributor_id'].value_counts()
print(max_recipes.head(1))
print('_' * 100)

""" 
Выполнила: Матвейчук
4.2 Посчитайте средний рейтинг к каждому из рецептов. Для скольких рецептов 
отсутствуют отзывы? Обратите внимание, что отзыв с нулевым рейтингом 
или не заполненным текстовым описанием не считается отсутствующим.
"""
print('4.2 Посчитайте средний рейтинг к каждому из рецептов. Для скольких рецептов отсутствуют отзывы')
reviews = pd.read_csv('../../data/reviews_sample.csv', delimiter=',', header=0)
reviews = reviews.drop(['user_id', 'date', 'Unnamed: 0'], axis='columns').groupby('recipe_id').mean()
reviews = reviews.groupby('recipe_id').mean()
print(reviews)
print('Количество рецептов с отсутствующими отзывами:', len(reviews[(reviews['rating'] == 0.000000)]))
print('_' * 100)

"""
Выполнила: Матвейчук
4.3 Посчитайте количество рецептов с разбивкой по годам создания.
"""
print('4.3 Посчитайте количество рецептов с разбивкой по годам создания')
recipes = pd.read_csv('../../data/recipes_sample.csv', delimiter=',')
recipes['submitted'] = [x[:4] for x in recipes['submitted'].tolist()]
print('год создания и количество рецептов: \n', recipes['submitted'].value_counts())
print('_' * 100)

"""
Выполнила: Кусакина
5.1 При помощи объединения таблиц, создайте `DataFrame`, состоящий из четырех 
столбцов: `id`, `name`, `user_id`, `rating`. Рецепты, на которые не оставлен 
ни один отзыв, должны отсутствовать в полученной таблице. Подтвердите 
правильность работы вашего кода, выбрав рецепт, не имеющий отзывов, 
и попытавшись найти строку, соответствующую этому рецепту, 
в полученном `DataFrame`.
"""
print('5.1 При помощи объединения таблиц, создайте `DataFrame`, состоящий из четырех столбцов: `id`, `name`, `user_id`, `rating`')
changed_recipes_df = recipes_df[['id', 'name']]
changed_reviews = reviews_df[reviews_df.review != np.nan]
changed_reviews_df = reviews_df[['recipe_id', 'user_id', 'rating']]
pd.options.mode.chained_assignment = None
changed_recipes_df.rename(columns={'id': 'recipe_id'}, inplace=True)
DataFrame = pd.merge(changed_recipes_df, changed_reviews_df)
print('полученная таблица\n', DataFrame)
print('_' * 100)

"""
Выполнила: Кусакина
5.2 При помощи объединения таблиц и группировок, создайте `DataFrame`, 
состоящий из трех столбцов: `recipe_id`, `name`, `review_count`, 
где столбец `review_count` содержит кол-во отзывов, оставленных 
на рецепт `recipe_id`. У рецептов, на которые не оставлен ни один 
отзыв, в столбце `review_count` должен быть указан 0. Подтвердите 
правильность работы вашего кода, выбрав рецепт, не имеющий отзывов, 
и найдя строку, соответствующую этому рецепту, в полученном `DataFrame`.
"""
print('5.2 При помощи объединения таблиц и группировок, создайте `DataFrame`, состоящий из трех столбцов')
DataFrame['review_count'] = DataFrame.groupby(['recipe_id'])['name'].transform('count')
changed_DataFrame = DataFrame.drop_duplicates(subset=['recipe_id'], keep='first')
changed_DataFrame = changed_DataFrame[['recipe_id', 'review_count']]
names_n_recipes = DataFrame.drop_duplicates(subset=['recipe_id'], keep='first')
names_n_recipes = names_n_recipes[['recipe_id', 'name']]
answer_DataFrame = pd.merge(names_n_recipes, changed_DataFrame)
print('полученный датафрейм:\n', answer_DataFrame)
print('_' * 100)

"""
Выполнила: Кусакина
5.3. Выясните, рецепты, добавленные в каком году, имеют наименьший средний рейтинг?
"""
print('5.3. Выясните, рецепты, добавленные в каком году, имеют наименьший средний рейтинг')
recipes_df.rename(columns={'id': 'recipe_id'}, inplace=True)
recipes_df_for_this_task = recipes_df[['recipe_id', 'submitted']]
reviews_df_for_this_task = reviews_df[['recipe_id', 'rating']]
print(recipes_df_for_this_task)
print(reviews_df_for_this_task)
DataFrame_for_task_5_3 = pd.merge(recipes_df_for_this_task, reviews_df_for_this_task)
DataFrame_for_task_5_3["year_submitted"] = DataFrame_for_task_5_3["submitted"].dt.to_period("Y")
DataFrame_for_task_5_3 = DataFrame_for_task_5_3[['recipe_id', 'year_submitted', 'rating']]
print(DataFrame_for_task_5_3)

reviews = DataFrame_for_task_5_3

sorted_reviews = sorted(set(reviews['recipe_id']))
idd = []
min_r = 5
print('Пожалуйста,подождите, производим подсчет...(займёт примерно секунд 40)')
for x in sorted_reviews:
    a = reviews.loc[reviews['recipe_id'] == x, 'rating'].mean()
    if a != 0 and a < min_r:
        min_r = a
        idd = [x]
    elif a == min_r:
        idd.append(x)
Answer1_df = DataFrame_for_task_5_3.loc[DataFrame_for_task_5_3['recipe_id'] == idd[0]]
Answer2_df = DataFrame_for_task_5_3.loc[DataFrame_for_task_5_3['recipe_id'] == idd[1]]
print('Самый низкий рейтинг-', min_r, ', id рецептов с самым низким рейтингом -', *idd)
print('Года с самым низким рейтингом:')
print(Answer1_df.iloc[0:1,1:2])
print(Answer2_df.iloc[0:1,1:2])
print('_' * 100)

"""
Выполнила: Гаевская
6.1 Отсортируйте таблицу в порядке убывания величины столбца `name_word_count`
и сохраните результаты выполнения заданий 3.1-3.3 в csv файл. 
"""
print('6.1 Отсортируйте таблицу в порядке убывания величины столбца `name_word_count`')
recipes = pd.read_csv('../../data/recipes_sample.csv', delimiter=',')

recipes['description_length'] = recipes['description'].str.len()
recipes['name'] = recipes['name'].str.capitalize()
recipes['name_word_count'] = recipes['name'].apply(lambda x: len(str(x).split(' ')))

recipes = recipes.sort_values(by=['name_word_count'])
print(recipes)

recipes.to_csv('new_recipes.csv', index=False)
print('_' * 100)

"""
Выполнила: Кусакина
6.2 Воспользовавшись `pd.ExcelWriter`, cохраните результаты 5.1 и 5.2 
в файл: на лист с названием `Рецепты с оценками` сохраните результаты 
выполнения 5.1; на лист с названием `Количество отзывов по рецептам` 
сохраните результаты выполнения 5.2.
"""
print('6.2 Воспользовавшись `pd.ExcelWriter`, cохраните результаты 5.1 и 5.2 в файл')
reviews = pd.read_csv('../../data/reviews_sample.csv')
recipes = pd.read_csv('../../data/recipes_sample.csv')
newtable = pd.concat((reviews, recipes), axis = 1)
newtable2 = newtable.dropna(subset=['review'])

rev = reviews.drop(['Unnamed: 0', 'user_id', 'date', 'rating', 'review'], axis=1)
rec = recipes.drop(['minutes', 'contributor_id', 'submitted', 'n_steps', 'description', 'n_ingredients'], axis=1)
rec = rec.rename(columns={"id": "recipe_id"})
new = pd.merge(rev, rec, on='recipe_id', how="outer")
new1 = new.groupby('recipe_id').size().reset_index(name='review_count')
new2 = pd.merge(new1, new, on='recipe_id', how="outer")

with pd.ExcelWriter('conclusion62.xlsx') as writer:
    newtable2.iloc[:, [7, 6, 1, 4]].to_excel(writer, sheet_name='Рецепты с оценками')
    new2.drop_duplicates().to_excel(writer, sheet_name='Количество отзывов по рецептам')
print('Выполнено', '_' * 100)
