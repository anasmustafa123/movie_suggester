import React from "react";

export default function Card() {
  return (
    <div class="card">
      <a href="movie-details.html?id=949567">
        <img
          src="https://image.tmdb.org/t/p/w500/so05qY0sDY0348bRg0tK9tSnnEq.jpg"
          class="card-img-top"
          alt="The Exorcism of Hannah Stevenson"
        ></img>
      </a>
      <div class="card-body">
        <h5 class="card-title">The Exorcism of Hannah Stevenson</h5>
        <p class="card-text">
          <small class="text-muted">Release: 2022-03-14</small>
        </p>
      </div>
    </div>
  );
}
