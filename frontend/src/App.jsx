//import reactLogo from './assets/react.svg'
import "./css/spinner.css";
import "./css/style.css";
import "./lib/fontawesome.css";
import "./lib/swiper.css";
import { useState } from "react";
import Search from "./components/Search";
import SimilarMovies from "./components/SimilarMovies";
function App() {
  const [selectedType, setSelectedType] = useState("movie");

  return (
    <>
      <Search selectedType={selectedType} setSelectedType={setSelectedType}></Search>
      <SimilarMovies type={selectedType}></SimilarMovies>
    </>
  );
}

export default App;
