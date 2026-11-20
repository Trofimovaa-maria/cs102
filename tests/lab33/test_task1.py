
from src.lab33.task1 import Movie, User, RecommendationSystem


def test_coincidences():
    """Проверка поиска общих фильмов."""
    user1 = User(1, [1, 2, 3, 4])
    user2 = User(2, [2, 3, 5, 6])

    system = RecommendationSystem([], [])

    result = system.coincidences(user1, user2)

    assert result == {2, 3}


def test_calculate_similarity():
    """Проверка расчёта степени сходства."""
    user1 = User(1, [1, 2, 3, 4])
    user2 = User(2, [2, 3, 5, 6])

    system = RecommendationSystem([], [])

    result = system.calculate_similarity(user1, user2)

    assert result == 0.5


def test_calculate_similarity_empty_history():
    """Проверка пользователя с пустой историей просмотров."""
    user1 = User(1, [])
    user2 = User(2, [1, 2, 3])

    system = RecommendationSystem([], [])

    result = system.calculate_similarity(user1, user2)

    assert result is None


def test_find_similar_users():
    """Проверка поиска похожих пользователей."""
    user1 = User(1, [1, 2, 3, 4])
    user2 = User(2, [1, 2, 5, 6])
    user3 = User(3, [1, 5, 6, 7])

    users = [user1, user2, user3]
    system = RecommendationSystem([], users)

    result = system.find_similar_users(user1, users)

    assert result == [user2]


def test_get_recommendations():
    """Проверка получения фильмов для рекомендации."""
    user1 = User(1, [1, 2, 3])
    user2 = User(2, [1, 2, 4, 5])
    user3 = User(3, [1, 2, 5, 6])

    users = [user1, user2, user3]
    system = RecommendationSystem([], users)

    result = system.get_recommendations(user1, users)

    assert result == {4, 5, 6}


def test_calculate_movie_weights():
    """Проверка расчёта весов фильмов."""
    user1 = User(1, [1, 2, 3, 4])
    user2 = User(2, [1, 2, 5])
    user3 = User(3, [1, 2, 5, 6])

    users = [user1, user2, user3]
    system = RecommendationSystem([], users)

    result = system.calculate_movie_weights(user1, users)

    assert result == {5: 1.0, 6: 0.5}


def test_max_recommendation():
    """Проверка выбора фильма с максимальным весом."""
    user1 = User(1, [1, 2, 3, 4])
    user2 = User(2, [1, 2, 5])
    user3 = User(3, [1, 2, 5, 6])

    users = [user1, user2, user3]
    system = RecommendationSystem([], users)

    result = system.max_recommendation(user1, users)

    assert result == 5


def test_max_recommendation_no_movies():
    """Проверка ситуации, когда нет фильмов для рекомендации."""
    user1 = User(1, [1, 2, 3])
    user2 = User(2, [1, 2, 3])

    users = [user1, user2]
    system = RecommendationSystem([], users)

    result = system.max_recommendation(user1, users)

    assert result is None


def test_get_movie_by_id():
    """Проверка поиска фильма по ID."""
    movie1 = Movie(1, "Inception")
    movie2 = Movie(2, "Interstellar")

    system = RecommendationSystem([movie1, movie2], [])

    result = system.get_movie_by_id(2)

    assert result == movie2


def test_get_movie_by_id_not_found():
    """Проверка ситуации, когда фильма нет в списке."""
    movie1 = Movie(1, "Inception")

    system = RecommendationSystem([movie1], [])

    result = system.get_movie_by_id(10)

    assert result is None


def test_recommend_movie():
    """Проверка итоговой рекомендации фильма."""
    movie1 = Movie(5, "Inception")
    movie2 = Movie(6, "Interstellar")

    user1 = User(1, [1, 2, 3, 4])
    user2 = User(2, [1, 2, 5])
    user3 = User(3, [1, 2, 5, 6])

    users = [user1, user2, user3]
    system = RecommendationSystem([movie1, movie2], users)

    result = system.recommend_movie(user1, users)

    assert result == movie1


def test_recommend_movie_no_recommendations():
    """Проверка итоговой рекомендации при отсутствии подходящих фильмов."""
    user1 = User(1, [1, 2, 3])
    user2 = User(2, [1, 2, 3])

    users = [user1, user2]
    system = RecommendationSystem([], users)

    result = system.recommend_movie(user1, users)

    assert result is None
