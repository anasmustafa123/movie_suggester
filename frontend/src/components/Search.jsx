import React, { useState } from "react";
import Autosuggest from "react-autosuggest";
import axios from "axios";
import { MagnifyingGlass } from "react-loader-spinner";

export default function Search({ selectedType, setSelectedType }) {
  const [search, setSearch] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [loading, setloading] = useState(false);

  const handleSetSearch = (event, { newValue }) => {
    setSearch(newValue);
  };

  const handleSetSelectedType = (event) => {
    setSelectedType(event.target.value);
  };

  const hangleSubmit = (event) => {
    event.preventDefault();
    // Handle form submission, e.g., make API request with search and selectedType
  };

  // Fetch suggestions based on the current input value
  const onSuggestionsFetchRequested = async ({ value }) => {
    // Implement your logic to fetch suggestions (e.g., from an API)
    // and update the suggestions state.
    console.log(value);
    setloading(true);
    if (value.length > 3) {
      const api_url =
        import.meta.env.VITE_SATATE == "production"
          ? import.meta.env.VITE_API_URL
          : import.meta.env.VITE_DEV_API_URL;
      let apiroute =
        selectedType == "movie"
          ? "/api/get_suggestions/movies"
          : "/api/get_suggestions/shows";
      try {
        let response;
        const res = await axios.post(
          `${api_url}${apiroute}`,
          {
            title: value,
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        response = await res.data;
        setloading(false);
        setSuggestions(response);
      } catch {
        console.error("Error posting data:");
      }
    }
    console.error("No posting data:");
  };
  // Clear suggestions when the input is cleared
  const onSuggestionsClearRequested = () => {
    setSuggestions([]);
  };

  // Render suggestion
  const renderSuggestion = (suggestion) => {
    return <div>{suggestion}</div>;
  };

  const inputProps = {
    placeholder: "Enter search term",
    value: search,
    onChange: handleSetSearch,
  };

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
            <Autosuggest
              suggestions={suggestions}
              onSuggestionsFetchRequested={onSuggestionsFetchRequested}
              onSuggestionsClearRequested={onSuggestionsClearRequested}
              getSuggestionValue={(suggestion) => suggestion}
              renderSuggestion={renderSuggestion}
              inputProps={inputProps}
            />
            <button className="btn" type="submit">
              <i className="fas fa-search"></i>
            </button>
          </div>
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
