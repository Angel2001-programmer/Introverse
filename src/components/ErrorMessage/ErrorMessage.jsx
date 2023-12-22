import styles from "./ErrorMessage.module.css";
import {Link} from "react-router-dom";

const ErrorMessage = () => {
    return(
            <div className={styles.messsage}>
                <h1>:(</h1>
                <p>Something Went Wrong</p>
                <button><Link to="/finalProject">Return to HomePage</Link></button>
            </div>
    )
}

export default ErrorMessage;