import styles from "./error.module.css"
import ErrorMessage from "../../components/ErrorMessage/ErrorMessage";

const Error = () => {
    return(
        <div className={styles.errorContainer}>
            <ErrorMessage />
        </div>
    )
}
export default Error;