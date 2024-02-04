import React, { useState } from "react";
import Autosuggest from "react-autosuggest";

export default function Search({selectedType, setSelectedType}) {
  const [search, setSearch] = useState("");
  const [suggestions, setSuggestions] = useState([]);

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
  const onSuggestionsFetchRequested = ({ value }) => {
    // Implement your logic to fetch suggestions (e.g., from an API)
    // and update the suggestions state.
    setSuggestions(["anas", "not anas"]);
  };

  // Clear suggestions when the input is cleared
  const onSuggestionsClearRequested = () => {
    setSuggestions([]);
  };

  // Render suggestion
  const renderSuggestion = (suggestion) => (
    <div>{suggestion}</div>
  );

  const inputProps = {
    placeholder: "Enter search term",
    value: search,
    onChange: handleSetSearch,
  };

  return (
    <section className="search">
      <div className="container">
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
        </form>
      </div>
    </section>
  );
}
