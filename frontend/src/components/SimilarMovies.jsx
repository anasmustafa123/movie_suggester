import React from "react";
import Card from "./Card";
import { useState } from "react";
export default function SimilarMovies(props) {
  const [names, setNames] = useState([0, 0, 0,0,0,0,0,0,0,0,0,0]);
  return (
    <section class="container">
      <h2>Similar {props.type}</h2>
      <div id="popular-movies" class="grid">
        {names.map((name) => (
          <Card></Card>
        ))}
      </div>
    </section>
  );
}
