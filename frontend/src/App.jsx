//import reactLogo from './assets/react.svg'
import "./css/spinner.css";
import "./css/style.css";
import "./lib/fontawesome.css";
import "./lib/swiper.css";
import { useState, useRef } from "react";
import Search from "./components/Search";
import SimilarMovies from "./components/SimilarMovies";

function App() {
  const [selectedType, setSelectedType] = useState("movie");
  const [getSimilar, setGetSimilar] = useState(false);
  const [loadingSimilarData, setLoadingSimilarData] = useState(false);
  const [similarData, setSimilarData] = useState([]);
  const execRef = useRef(null);
  const scrollToSimilarMovies = () => {
    execRef.current.scrollIntoView({ behavior: "smooth" });
  };
  return (
    <>
      <Search
        selectedType={selectedType}
        setSelectedType={setSelectedType}
        setGetSimilar={setGetSimilar}
        setLoadingSimilarData={setLoadingSimilarData}
        setSimilarData={setSimilarData}
        scrollToSimilarMovies={scrollToSimilarMovies}
      ></Search>
        <SimilarMovies
          type={selectedType}
          loadingSimilarData={loadingSimilarData}
          similarData={similarData}
          execRef={execRef}
        ></SimilarMovies>
    </>
  );
}

export default App;
