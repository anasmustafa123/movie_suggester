import React from "react";

export default function Card({key, data, tmdbLinkPrefix}) {
  return (
    <div key={key} class="card">
      <a href={tmdbLinkPrefix+data.id} target="_blank">
        <img
          src={data["poster_path"]}
          class="card-img-top"
          alt="The Exorcism of Hannah Stevenson"
        ></img>
      </a>
      <div class="card-body">
        <h5 class="card-title">{data.title}</h5>
      </div>
    </div>
  );
}
