# Vuex

> 상태 관리 전용 라이브러리

```js
export default new Vuex.Store({ key : value })
```

## 1. without Vuex

- 상태, 뷰, 액션 : 단방향 데이터 흐름
- 공통의 상태 공유 => 유지 보수 어려움 => 컴포넌트에서 공유된 상태를 추출, 전역으로 관리 => Vuex
- `store.state`로 접근
- `store.commit` 메서드로 상태 변경을 트리거

## 2. Store

### 특징

- Vuex store는 반응형
- `저장소의 state` 직접 변경 불가 => `commit을 이용한 mutation` => 모든 상태 추적 가능
  - `store.commit('뮤테이션함수')`

### 2.1 state

> 데이터의 집합

### 2.2 getters

>  state를 (가공해서)가져올 함수들. **=== computed**

### 2.3 mutations 

>  state를 변경하는 함수들

- mutations에 작성되지 않은 state 변경 코드들은 모두 동작 X
- 모든 mutations 함수들은 동기적으로 동작하는 코드.all
- `commit`을 통해 실행

### 2.4 actions

> 범용적인 함수들

- mutations에 정의한 함수를 actions에서 실행 가능
- 비동기 로직은 actions에서 정의
- `dispatch`를 통해 실행

```javascript
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

// eslint-disable-next-line no-undef
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;
const API_URL = 'https://www.googleapis.com/youtube/v3/search';

export default new Vuex.Store({
	// data 의 집합(중앙 관리할 모든 데이터===상태)
	state: {
		inputValue: '',
		videos: [],
		selectedVideo: null,
	},
	// state 를 (가공해서)가져올 함수들. === computed
	getters: {
		videoUrl(state) {
			return `https://youtube.com/embed/${state.selectedVideo.id.videoId}`;
		},
		videoTitle: state => state.selectedVideo.snippet.title,
		videoDescription: state => state.selectedVideo.snippet.description,
	},
	// state 를 변경하는 함수들(mutations 에 작성되지 않은 state 변경 코드는 모두 동작하지 않음.)
	// 모든 mutation 함수들은 동기적으로 동작하는 코드.all
	// commit 을 통해 실행함.
	mutations: {
		setInputValue(state, inputValue) {
			state.inputValue = inputValue;
		},
		setVideos(state, videos) {
			state.videos = videos;
		},
		setSelectedVideo(state, video) {
			state.selectedVideo = video;
		},
	},
	// 범용적인 함수들. mutations 에 정의한 함수를 actions 에서 실행 가능.
	// 비동기 로직은 actions 에서 정의.
	// dispatch 를 통해 실행함
	actions: {
		fetchVideos({ commit, state }, event) {
			// 1. inputValue 를 바꾼다.
			commit('setInputValue', event.target.value);
			// 2. state.inputValue 로 요청보낸다.
			axios
				.get(API_URL, {
					params: {
						key: API_KEY,
						part: 'snippet',
						type: 'video',
						q: state.inputValue,
					},
				})
				.then(res => {
					res.data.items.forEach(item => {
						const parser = new DOMParser();
						const doc = parser.parseFromString(item.snippet.title, 'text/html');
						item.snippet.title = doc.body.innerText;
					});
					// 3. state.videos 를 응답으로 바꾼다.
					commit('setVideos', res.data.items);
				})
				.catch(err => console.error(err));
		},
	},
	modules: {},
});

```

## 3. 핵심 컨셉

## 3.1 상태

### 3.2 단일 상태 트리

- 각 애플리케이션마다 하나의 저장소, 디버깅을 위한 현태 앱 상태 스냅 샷을 쉽게 가져올 수 있다
- 모듈성과 충돌X
