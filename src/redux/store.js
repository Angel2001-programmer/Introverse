import { configureStore } from "@reduxjs/toolkit";
import userReducer from "./slices/userSlice";
import storage from "redux-persist/lib/storage";
import { combineReducers } from "@reduxjs/toolkit";
import { persistReducer } from "redux-persist";
// import thunk from "redux-thunk";

const reducers = combineReducers({
  auth: userReducer,
});

const persistConfig = {
  key: "root",
  storage,
};

const persistedReducer = persistReducer(persistConfig, reducers);

const store = configureStore({
  reducer: persistedReducer,
  devTools: process.env.NODE_ENV !== "production",
  // middleware: [thunk],
});

export default store;

// Old ones, first one def works
// export default configureStore({
//   reducer: {
//     auth: userReducer,
//   }
// })

// export const store = configureStore({
//     reducer: userReducer,
// })