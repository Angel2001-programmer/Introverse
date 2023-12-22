import styles from "./MobileNav.module.css";
import { Link } from "react-router-dom";
import { NewUserContext, MobileNavContext, StyleMobileNavContext, UserContext} from "../../components/FinalProject/FinalProject";
import { useContext, useState } from "react";


// Angel, can you update this one to match the login requirements of the other navbar too? Although I don't think mobile functionality is a prio for submission
const MobileNav = () => {
    const [newUser, setNewUser] = useContext(NewUserContext);
    const [isMobileClicked, setIsMobileClicked] = useContext(MobileNavContext);
    const [isOpened, setIsOpened] = useContext(UserContext);

    let style2 = StyleMobileNavContext;

    if (!isMobileClicked){
        style2 = {display: 'none'};
    } else {
        style2 = {display: 'block'};
    }

    return(
        <div className={styles.MobileNav} style={style2}>
        {newUser ?
        <div className={styles.navItemsMobile}>
          <div className={styles.navItemMobile}>
          <Link className={styles.navLink} to={"/finalProject"} onClick={() => setIsMobileClicked(false)}>Home</Link>
          </div>
          <div className={styles.navItemMobile}>
          <Link className={styles.navLink} to="/recommendations" onClick={() => setIsMobileClicked(false)}>Recommendations</Link>
          </div>
          <div className={styles.navItemMobile}>
          <Link className={styles.navLink} to="/about" onClick={() => setIsMobileClicked(false)}>About</Link>
          </div>
          <div className={styles.navItemMobile}>
          <Link className={styles.navLink} to="/forums" onClick={() => setIsMobileClicked(false)}>Forums</Link>
          </div>
          <div className={styles.navItemMobile}>
          <Link className={styles.navLink} to="/profile" onClick={() => setIsMobileClicked(false)}>Profile</Link>
          </div>
          <div className={styles.navItemMobile}>
          <Link className={styles.navLink} onClick={() => {
            setNewUser(false) 
            setIsMobileClicked(false)}}
            >Sign Out</Link>
          </div>
        </div>:
        <div className={styles.navItemsMobile}>
            <div className={styles.navItemMobile}>
          <Link className={styles.navLink} to="/finalProject" onClick={() => setIsMobileClicked(false)}>Home</Link>
          </div>
          <div className={styles.navItemMobile}>
          <Link className={styles.navLink} to={"/about"} onClick={() => setIsMobileClicked(false)}>About</Link>
          </div>
          {/* Will implement tomorrow. */}
          <div className={styles.navItemMobile}>
          <Link className={styles.navLink} to={null} onClick={() => {
            setIsOpened(true);
            setIsMobileClicked(false)}}
            >Sign in</Link>
          </div>
        </div>
        }
    </div>
    )
}

export default MobileNav