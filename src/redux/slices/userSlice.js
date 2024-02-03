import { createSlice } from "@reduxjs/toolkit";

const userSlice = createSlice({
  name: 'auth',
  initialState: { user: {}, },
  reducers: {
    setSignIn: (state, action) => {
      state.user = {...state.user, ...action.payload}
    },
    setSignOut: (state) => {
      state.user = {}
    }
  },
})

export const { setSignIn, setSignOut } = userSlice.actions
export default userSlice.reducer

export const selectCurrentUser = (state) => state.auth.user