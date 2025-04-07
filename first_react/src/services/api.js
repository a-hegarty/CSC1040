const API_KEY = "c9fbac6c8d909d4eeef5489a17d25e4f";
const BASE_URL = "https://api.themoviedb.org/3";

export const getPopMovies = async() =>{
    const response = await fetch(`${BASE_URL}/movie/popular?api_key=${API_KEY}`);
    const data = response.json();
    return data.results;
};

export const searchMovies = async(query) => {
    const response = await fetch(`${BASE_URL}/movie/popular?api_key=${API_KEY}&query=${encodeURIComponent(query)}`);
    const data = response.json();
    return data.results;
};