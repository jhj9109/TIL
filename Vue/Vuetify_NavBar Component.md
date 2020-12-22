### Vuetify_AppBar_Navigation Drawers

- NavBar 와 알람 토글 기능의 Navigation Drawers

- [참고 예제](https://vuetifyjs.com/en/components/app-bars/#toggle-navigation-drawers)

- `drawer` 의 Boolean 값을 기준으로 알림창이 생성된다

  - 초기값은 false로 준다.
  - 한번의 토글링 이후 `MouseEvent`를 가리킨다.
  - MouseEvent 

- 내부적으로 `input`, `transitioned` 이름의 `$emit`이 발생한다

  - `input` : `Boolean` 값이 `payload` 로 전달되며, 이것이 `drawer` 의 값을 조절하는듯 하다.
  - `transitioned` : `transition` 되는 이팩트와 관련이 있는것 같다.

  ```vue
  <div id="app">
    <v-app id="inspire">
      <v-card class="mx-auto overflow-hidden"height="400">
  
        <v-app-bar color="deep-purple" dark  >
          <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
          <v-toolbar-title>Title</v-toolbar-title>
        </v-app-bar>
    
        <v-navigation-drawer v-model="drawer" absolute temporary>
          <v-list nav dense>
            <v-list-item-group v-model="group" active-class="deep-purple--text text--accent-4" >
              <v-list-item> 1 </v-list-item>
              <v-list-item> 2 </v-list-item>  
            </v-list-item-group>
          </v-list>
        </v-navigation-drawer>
      </v-card>
    </v-app>
  </div>
  ```

  
