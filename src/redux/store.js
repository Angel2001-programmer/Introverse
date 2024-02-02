import { configureStore } from "@reduxjs/toolkit";
import userReducer from "./slices/userSlice";

// export const store = configureStore({
//     reducer: userReducer,
// })

export default configureStore({
    reducer: {
        auth: userReducer,
    }
})