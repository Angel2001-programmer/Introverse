import styles from "./recommendations.module.css"
import React, { Fragment, useEffect } from 'react'
import Button from "../../UI/Button/button";
import { useState } from "react";
import axios from "axios";
import NavBar from "../../components/NavBar/navbar";
import MobileNav from "../../components/MobileNav/MobileNav";
import DropDownMenu from "../../components/DropDownMenu/dropDownMenu";

const Recommendations = () => {
  const tempList = [{text: "Anime"}, {text: "Games"}, {text: "Books"}]
  const [GenreTitle, setGenreTitle] = useState('')
  const [List, setList] = useState([])
  const [isClicked, setisClicked] = useState(false)
  const [isPressed, setIsPressed] = useState(false);
  let route = '';

  const formatter = new Intl.NumberFormat('en-UK', {
    style: 'currency',
    currency: 'GBP',
  
    // These options are needed to round to whole numbers if that's what you want.
    //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
    //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
  });

  const SelectedGenre = (title) => {
    setGenreTitle(title);
    setisClicked(true);
  }

  let listComponent = null;
  try {
    switch(GenreTitle){
      case "Anime":
        route = "anime_suggestions"
        listComponent = <Fragment>
        {List.map((item) => 
        <div key={item.Anime_ID} className={styles.Container} style={{backgroundColor: "white"}}>
            <div className={styles.rowContainer}>
            <div className={styles.ColumnContainer}>
            <h3>Name: {item.Anime_Name}</h3>
            <h3>Genre: {item.Anime_Genre}</h3>
            <h5>Description: {item.Anime_Script}</h5>
            <h3>You can find this on {item.Where_TW}</h3>
            </div>
            </div>
         </div>
         )}
      </Fragment>
        break;
      case "Books":
        route = "book_suggestions"
        listComponent = <Fragment>
       {List.map((item) => 
        <div key={item.Books_ID} className={styles.Container} style={{backgroundColor: "white"}}>
            <div className={styles.rowContainer}>
            <div className={styles.ColumnContainer}>
            <h3>Name: {item.Book_Name}</h3>
            <h3>Genre: {item.Book_Genre}</h3>
            <h5>Description: {item.Book_Script}</h5>
            <h5>Auther: {item.Book_Author}</h5>
            <h5>Price: {formatter.format(item.Price)}</h5>
            </div>
            </div>
         </div>
         )}
         </Fragment>
        break;
      case "Games":
        route = "games_suggestions"

          listComponent = <Fragment>
       {List.map((item) => 
        <div key={item.Game_ID} className={styles.Container} style={{backgroundColor: "white"}}>
            <div className={styles.rowContainer}>
            <div className={styles.ColumnContainer}>
            <h3>Name: {item.Game_Name}</h3>
            <h3>Genre: {item.Game_Genre}</h3>
            <h5>Description: {item.Game_Script}</h5>
            <h5>{formatter.format(item.Price)}</h5>
            <h3>You can play on {item.W_Console}</h3>
            </div>
            </div>
         </div>
         )}
         </Fragment>
          break;
        default:
          listComponent = <h3 className={styles.errorMessage}>Something went wrong please try again later!</h3>
        break;
    }
  } catch(e){
    listComponent = <h3 className={styles.errorMessage}>Something went wrong please try again later!</h3>
  }

  useEffect(() => {
    const getAPI = async () => {
      try{
        const response = await axios.get('http://localhost:5000/' + route);
        setList(response.data);
        console.log(List);
      } catch (error) {
        setList(null);
        console.log(error)
        listComponent = <h3 className={styles.errorMessage}>Something went wrong please try again later!</h3>
      }
    }
    getAPI();
  }, [GenreTitle])

return (
    <div>
      <NavBar isPressed={isPressed} onChangePressed={setIsPressed}/>
      <DropDownMenu isPressed={isPressed} setIsPressed={setIsPressed}/>
      <MobileNav/>
    <div className={styles.Page}>
      {!isClicked?
      <div className={styles.Container}>
          {tempList.map((Genre) => 
            <Button key={Genre.text} text={Genre.text} paddingToLeft="25vh" paddingToRight="25vh" click={() => SelectedGenre(Genre.text)}/>
          )}
      </div>
      : 
      <Fragment>
        <div className={styles.topMenu}>
        <h2 className={styles.title} onClick={() => setisClicked(false)} style={{cursor: "pointer"}}>←</h2>
        <h2 className={styles.title}>{GenreTitle}</h2></div>
      <div className={styles.ContainerMain}> 
      {listComponent}
      </div>
      </Fragment>
      }  
      </div>
      </div>
  )
}  
export default Recommendations;
       