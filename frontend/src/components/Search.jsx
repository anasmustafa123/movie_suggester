import React, { useState, useEffect } from "react";
import axios from "axios";
import { MagnifyingGlass } from "react-loader-spinner";

export default function Search({
  selectedType,
  setSelectedType,
  setGetSimilar,
  setLoadingSimilarData,
  setSimilarData,
  scrollToSimilarMovies,
}) {
  const [search, setSearch] = useState("");
  const [loading, setloading] = useState(false);
  const [allMovies, setAllMovies] = useState([]);
  const [allShows, setAllShows] = useState([]);

  useEffect(() => {
    async function fetchData() {
      setloading(true);
      const api_url =
        import.meta.env.VITE_SATATE == "production"
          ? import.meta.env.VITE_API_URL
          : import.meta.env.VITE_DEV_API_URL;
      const movieRes = await axios.post(
        `${api_url}/api/get_movies`,
        {},
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      setAllMovies(await movieRes.data);
      if (selectedType === "movie") {
        setloading(false);
      }
      const showRes = await axios.post(
        `${api_url}/api/get_shows`,
        {},
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      setAllShows(await showRes.data);
      setloading(false);
    }
    fetchData();
  }, []);

  const handleSetSearch = (event) => {
    setSearch(event.target.value);
  };

  const handleSetSelectedType = (event) => {
    setSelectedType(event.target.value);
  };

  const hangleSubmit = async (event) => {
    event.preventDefault();
    let response;
    setLoadingSimilarData(true);
    setGetSimilar(true);
    scrollToSimilarMovies();
    // Handle form submission, e.g., make API request with search and selectedType
    try {
      const api_url =
        import.meta.env.VITE_SATATE == "production"
          ? import.meta.env.VITE_API_URL
          : import.meta.env.VITE_DEV_API_URL;
      let apiroute =
        selectedType == "movie" ? "/api/similar_movies" : "/api/similar_shows";
      const res = await axios.post(
        `${api_url}${apiroute}`,
        { title: search, n: 13 },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      response = await res.data;
      setSimilarData(response);
      setLoadingSimilarData(false);
    } catch (error) {}
  };

  const inputProps = {
    placeholder: "Enter search term",
    value: search,
    onChange: handleSetSearch,
  };
  function onSuggestionsFetchRequested(list) {
    return list.filter((str) => {
      return str.toLowerCase().includes(search.toLowerCase());
    });
  }
  return (
    <section className="search">
      <div className="search-container container">
        <div id="alert"></div>
        <form onSubmit={hangleSubmit} className="search-form">
          <div className="search-radio">
            <input
              checked={selectedType === "movie"}
              onChange={handleSetSelectedType}
              type="radio"
              id="movie"
              name="type"
              value="movie"
            />
            <label htmlFor="movie">Movies</label>
            <input
              checked={selectedType === "tv"}
              onChange={handleSetSelectedType}
              type="radio"
              id="tv"
              name="type"
              value="tv"
            />
            <label htmlFor="tv">TV Shows</label>
          </div>
          <div className="search-flex">
            <input
              autocomplete="off"
              type="text"
              id="myInput"
              onChange={(e) => {
                handleSetSearch(e);
              }}
              value={search}
              placeholder="Search for names.."
            />
            <button className="btn" type="submit">
              <i className="fas fa-search"></i>
            </button>
          </div>
          {search !== "" && (
            <ul id="myUL">
              {selectedType === "movie"
                ? onSuggestionsFetchRequested(allMovies)
                    .slice(0, 7)
                    .map((v, i) => (
                      <li onClick={() => setSearch(v)} key={i}>
                        <a href="#">{v}</a>
                      </li>
                    ))
                : onSuggestionsFetchRequested(allShows)
                    .slice(0, 7)
                    .map((v, i) => (
                      <li onClick={() => setSearch(v)} key={i}>
                        <a href="#">{v}</a>
                      </li>
                    ))}
            </ul>
          )}

          {loading && (
            <MagnifyingGlass
              visible={true}
              height="80"
              width="80"
              ariaLabel="magnifying-glass-loading"
              wrapperStyle={{}}
              wrapperClass="magnifying-glass-wrapper"
              glassColor="#c0efff"
              color="#e15b64"
            />
          )}
        </form>
      </div>
    </section>
  );
}
