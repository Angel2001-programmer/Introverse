import ListItem from "../ListItem/listItem";
import styles from "./CardList.module.css";

const CardList = props => {
    return(
        <div className={styles.CardContainer}>
            <div className={styles.CardRow}>
            {props.data.map((item) => {
            return <ListItem 
                        key={item.id}
                        image={item.image} 
                        name={item.name} 
                        description={item.description}
                    />
            })}
            </div>
        </div>
    )
}

export default CardList;