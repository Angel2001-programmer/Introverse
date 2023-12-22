import styles from "./HomeList.module.css";
import HomeItem from "../HomeItem/HomeItem";
const HomeList = (props) => {
    return(
    <div className={styles.row}>
        {props.list.map((item => 
            <HomeItem
            key={item.id}
            text={item.text} 
            image={item.image} 
            alt={item.alt}
            />
            
        ))}  
    </div>
    )    
}

export default HomeList;