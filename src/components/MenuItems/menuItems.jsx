import styles from "./menuItem.module.css";
import { Link } from "react-router-dom";

const MenuItems = () => {
    return(
        <ul>
            <li className={styles.item}><Link to="/home">Home</Link></li>
            <li className={styles.item}><Link to="/finalProject">About</Link></li>
            <li className={styles.item}><Link to="/contact">Contact</Link></li>
        </ul>
    )
}

export default MenuItems;