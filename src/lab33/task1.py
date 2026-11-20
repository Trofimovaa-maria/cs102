import typing as tp


class Movie:
    """Класс для хранения информации о фильме."""

    def __init__(self, movie_id: int, title: str) -> None:
        """
        Создать объект фильма.

        movie_id: уникальный идентификатор фильма
        title: название фильма
        """
        self.movie_id = movie_id
        self.title = title


class User:
    """Класс для хранения информации о пользователе."""

    def __init__(self,user_id: int, watched_movies: tp.List[int]) -> None:
        """
        Создать объект пользователя.

        user_id: уникальный идентификатор пользователя
        watched_movies: список ID просмотренных фильмов
        """
        self.user_id = user_id
        self.watched_movies = watched_movies


class RecommendationSystem:
    """
    Класс рекомендательной системы фильмов.

    Позволяет находить похожих пользователей,
    рассчитывать веса фильмов и формировать рекомендации.
    """

    def __init__(self,movies: tp.List[Movie],users: tp.List[User]) -> None:
        """
        Создать рекомендательную систему.

        movies: список доступных фильмов
        users: список пользователей
        """
        self.movies = movies
        self.users = users


    def coincidences(self,user1: User, user2: User) -> tp.Set[int]:
        """
        Найти фильмы, просмотренные обоими пользователями.
        """
        return set(user1.watched_movies) & set(user2.watched_movies)

    def calculate_similarity(self,user1: User,user2: User) -> tp.Optional[float]:
        """
        Рассчитать степень сходства двух пользователей.

        user1: пользователь, для которого ищем рекомендации
        user2: пользователь для сравнения
        return: доля совпадений или None, если история user1 пуста
        """
        if len(user1.watched_movies) == 0:
            return None

        return len(self.coincidences(user1, user2)) / len(user1.watched_movies)

    def find_similar_users(self,user1: User,users: tp.List[User]) -> tp.List[User]:
        """
        Найти пользователей со степенью сходства не менее 50%.

        user1: пользователь, для которого ищем рекомендации
        users: список пользователей для сравнения
        return: список похожих пользователей
        """
        similar_users = []

        for user in users:
            if user is user1:
                continue

            similarity = self.calculate_similarity(user1, user)

            if similarity is not None and similarity >= 0.5:
                similar_users.append(user)

        return similar_users

    def get_recommendations(self,user1: User,users: tp.List[User]) -> tp.Set[int]:
        """
        Получить список уникальных фильмов для рекомендации.

        Исключает фильмы, которые пользователь уже смотрел.
        return: множество ID рекомендованных фильмов
        """
        recommended_movies = set()

        for user in self.find_similar_users(user1, users):
            for movie in user.watched_movies:
                if movie in user1.watched_movies:
                    continue

                recommended_movies.add(movie)

        return recommended_movies

    def calculate_movie_weights(self,user1: User,users: tp.List[User]) -> tp.Dict[int, float]:
        """
        Рассчитать итоговые веса рекомендованных фильмов.

        Вес фильма равен сумме коэффициентов сходства
        всех пользователей, которые его смотрели.

        return: словарь, где ключ — ID фильма, значение — его вес
        """
        movie_weights = {}

        for user in self.find_similar_users(user1, users):
            similarity = self.calculate_similarity(user1, user)

            for movie in user.watched_movies:
                if movie in user1.watched_movies:
                    continue

                if movie in movie_weights:
                    movie_weights[movie] += similarity
                else:
                    movie_weights[movie] = similarity

        return movie_weights

    def max_recommendation(self,user1: User,users: tp.List[User]) -> tp.Optional[int]:
        """
        Найти ID фильма с максимальным весом.

        return: ID фильма с максимальным весом или None
        """
        movie_weights = self.calculate_movie_weights(user1, users)

        if not movie_weights:
            return None

        best_movie = max(movie_weights.items(), key=lambda item: item[1])

        return best_movie[0]

    def get_movie_by_id(self, movie_id: int) -> tp.Optional[Movie]:
        """
        Найти фильм по его идентификатору.

        movie_id: ID искомого фильма
        return: объект фильма или None, если фильм не найден
        """
        for movie in self.movies:
            if movie.movie_id == movie_id:
                return movie

        return None

    def recommend_movie(self,user1: User,users: tp.List[User]) -> tp.Optional[Movie]:
        """
        Сформировать итоговую рекомендацию для пользователя.

        return: объект рекомендованного фильма или None
        """
        movie_id = self.max_recommendation(user1, users)

        if movie_id is None:
            return None

        return self.get_movie_by_id(movie_id)


