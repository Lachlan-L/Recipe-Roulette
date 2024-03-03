import React, { useState } from "react";
import './Roulette.css';
import apple from './assets/apple.png';
import banana from "./assets/banana.png";
import grape from "./assets/grape.png";
import pumpkin from "./assets/pumpkin.png";
import meat from "./assets/meat.png";
import carrot from "./assets/carrot.png";
import steak from "./assets/steak.png";
import chicken from "./assets/chicken.png";
import fish from "./assets/fish.png";
import { useNavigate } from "react-router-dom";
import './bubble-right.css';

const options = ['Vegetables', 'Seafood', 'Fruit', 'Meat'];
const imageOptions = [banana, grape, pumpkin, meat, carrot, steak, chicken, fish, apple];
const linkOptions = ['/', 'spin', 'recipe'];  // this is a placeholder, remove later

const Roulette = () => {
  const [selections, setSelections] = useState(Array(3).fill('Vegetables'));
  const [images, setImages] = useState(Array(3).fill(apple));
  const [clicked, setClicked] = useState(false);
  const [names, setNames] = useState(Array(3).fill('Brussel Sprouts'));
  const [costs, setCosts] = useState(Array(3).fill(0));
  const [links, setLinks] = useState(Array(3).fill('/'))
  const navigate = useNavigate();

  const handleSpinAll = () => {
    setClicked(true);
    for (let index = 0; index < images.length; index++) {
      handleReroll(index);
    }
  };

  const handleReroll = (index) => {
    let counter = 0;
    const interval = setInterval(() => {
      setImages((currentImages) => currentImages.map((img, i) => {
        if (i === index) {
          return imageOptions[Math.floor(Math.random() * imageOptions.length)];
        }
        return img;
      }));
  
      counter++;
      if (counter > 10) {
        clearInterval(interval);
        showIngredient(index);
      }
    }, 100);
  };

  const setSelection = (value, index) => {
    setSelections(choices => 
      choices.map((item, i) => i === index ? value : item)
    );
  }

  const recipe = () => {
    navigate('/recipe');
  }

  const showIngredient = (index) => {
    setImages((currentImages) => currentImages.map((img, i) => {
      if (i === index) {
        return imageOptions[Math.floor(Math.random() * imageOptions.length)]; // change this to img of ingredient from backend
      }
      return img;
    }));
    setNames((currentNames) => currentNames.map((name, i) => {
      if (i === index) {
        return options[Math.floor(Math.random() * options.length)]; // change this to name of ingredient from backend
      }
      return name;
    }));
    setCosts((currentCosts) => currentCosts.map((cost, i) => {
      if (i === index) {
        return Math.floor(Math.random() * 100); // change this to cost of ingredient from backend
      }
      return cost;
    }));
    setLinks((currentLinks) => currentLinks.map((link, i) => {
      if (i === index) {
        return linkOptions[Math.floor(Math.random() * linkOptions.length)]; // change this to link of ingredient from backend
      }
      return link;
    }));
  }

  return (
    <div className="page">
      <div className="container">
        <h1 className="title">Test Your Luck</h1>
        <div className="box-row">
          {images.map((imageSrc, index) => (
            <div key={index} className="box-container">
              <div className="box">
                {clicked &&<p className="ing-name">{names[index]}</p>}
                {!clicked &&<img src={imageSrc} alt={`Slot ${index}`} />}
                {clicked &&<a href={links[index]} target="_blank" rel="noopener noreferrer">
                  <img src={imageSrc} alt={`Slot ${index}`} />
                </a>}
                {clicked &&<p className="ing-cost">${costs[index]}</p>}
              </div>
              {clicked && <button className="rerollButton" onClick={() => handleReroll(index)}>Reroll</button>}
              <div class="select-wrapper">
                <select class="drop-down" value={selections[index]} onChange={e => setSelection(e.target.value, index)}>
                  {options.map(option => (
                    <option key={option} value={option}>{option}</option>
                  ))}
                </select>
            </div>
            </div>
          ))}
        </div>
        <button onClick={handleSpinAll} className="spinButton btn-22 spinType"><span>Spin All</span></button>
        {clicked &&<button onClick={recipe} className="btn-22 recipeButton recipeType"><span>Find Recipe</span></button>}
      </div>
    </div>
  );
};

export default Roulette;