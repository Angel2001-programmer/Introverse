import { Fragment, useState, useContext } from 'react'
import NavBar from '../../components/NavBar/navbar';
import styles from "./home.module.css";
import HomeItem from "../../components/HomeItem/HomeItem";
import Community from "../../assets/images/logos/community.png"
import Gaming from "../../assets/images/logos/gaming.png"
import Books from "../../assets/images/logos/books.png"
import Friendship from "../../assets/images/logos/friendship.png"
import TreatOthers from "../../assets/images/logos/treatothers.png"
import News from "../../assets/images/logos/discussions.png"
import { NewUserContext } from "../../components/FinalProject/FinalProject";
import DropDownMenu from "../../components/DropDownMenu/dropDownMenu";
import MobileNav from '../../components/MobileNav/MobileNav';
import Landing from "../../components/landing/landing";

export default function Home() {  
  const [isPressed, setIsPressed] = useState(false);
  // const [newUser, setNewUser] = useContext(NewUserContext);
  return (
    <Fragment>
    <NavBar isPressed={isPressed} onChangePressed={setIsPressed}/>
    <DropDownMenu isPressed={isPressed} setIsPressed={setIsPressed}/>
    <MobileNav/>
    <Landing/>
    <div className={styles.container0}>
      <HomeItem text="A friendly place for introverts and everyone to express themseleves in safe a good environment" image={Community}/>
      <HomeItem text="A place for gamers of all kinds ranging from PC, Xbox, Playstation and much more!" image={Gaming}/>
      <HomeItem text="A place for book readers, to discuss there most loved pages." image={Books}/>
    </div>
    <div className={styles.container1}>
      <HomeItem text="This is a place where you can find guidance and support if you are having a tough time," image={Friendship}/>
      <HomeItem text="All we ask is you treat users on this website with respect and how you wish to be treated!" image={TreatOthers}/>
      <HomeItem text="We have plenty of anime discussion and news. you won’t want to miss this!" image={News}/>
    </div>
    </Fragment>
  )
}
