import React from "react";
import Card from "./Card";
import { DNA } from "react-loader-spinner";

export default function SimilarMovies(props) {
  console.log({ props });
  return (
    <section ref={props.execRef} class="container">
      <h2>Similar {props.type}</h2>
      <div id="popular-movies" class="grid">
        {props.loadingSimilarData
          ? new Array(12).fill(null).map((value, i) => (
              <DNA
                visible={true}
                height="200"
                width="200"
                ariaLabel="dna-loading"
                wrapperStyle={{}}
                wrapperClass="dna-wrapper"
              />
            ))
          : props.similarData.map((value, i) => (
              <Card data={value} key={i}></Card>
            ))}
      </div>
    </section>
  );
}
