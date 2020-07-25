const Header = ()=>import( '@/components/public/Header')
const Footer = ()=>import( '@/components/public/Footer')
const Home = ()=>import( '@/components/home/Home')

const homeView = ()=>import( '@/components/home/views/home')
const netRecommendView = ()=>import( '@/components/home/views/netRecommend')

const userMenuCard = ()=>import('@/components/home/cards/userMenu')
const upLoadCard = ()=>import('@/components/home/cards/upLoad')
const fileListCard = ()=>import('@/components/home/cards/fileListCard')
const askMsgListCard = ()=>import('@/components/home/cards/askMsgList')
const teamMsgListCard = ()=>import('@/components/home/cards/teamMsgList')
const showFilesCard = ()=>import('@/components/home/cards/showFilesCard')
const knowNetCard = ()=>import('@/components/home/cards/knowNet')
const recommendCard = ()=>import('@/components/home/cards/recommend')
const dynamicCard = ()=>import('@/components/home/cards/dynamic')

const friendsView = ()=>import('@/components/home/friends/views/friends')
const friendsMenuView = ()=>import('@/components/home/friends/views/friendsMenu')
const followerCard = ()=>import('@/components/home/friends/cards/follower')
const followingCard = ()=>import('@/components/home/friends/cards/following')
const friendInfoCard = ()=>import('@/components/home/friends/cards/friendInfo')
const friendFinderCard = ()=>import('@/components/home/friends/cards/friendFinder')
const talkBoxCard = ()=>import('@/components/home/friends/cards/talkBox')
const initBoxCard = ()=>import('@/components/home/friends/cards/initBox')

const homeRouter = {
	path: '/home',
	components: { 
		header: Header,
		main: Home,
		footer: Footer,
		default: Home,
	},
	children: [{
		path: '',
		components: {
			menu: userMenuCard,
			views: homeView, 
			default: homeView,
		},
		children: [{
			path: '', meta: { requireAuth: true },
			components: {
				upLoad: upLoadCard,
				fileList: fileListCard,
				msgList: askMsgListCard,
				teamMsgList: teamMsgListCard,
				showFiles: showFilesCard,
				netRecommend: netRecommendView,
			},
			children: [{	
				path: '', name: 'homedefault', meta: { requireAuth: true },
				components: {
					knowNet: knowNetCard,
					recommend: recommendCard,
					dynamic:dynamicCard,
				}
			}]
		}]
	}, {
		path: 'friends',
		components: {
			menu: friendsMenuView, 
			views: friendsView,
			default: friendsView,
		},
		children: [{
			path: '', name: 'friendsDefault', meta: { requireAuth: true },
			components: {
				follower: followerCard,
				following: followingCard,
				friendInfo: friendInfoCard,
				initBox: initBoxCard,
				talkBox: talkBoxCard,
				default: friendInfoCard,
			}
		}, {
			path: 'talk', name: 'friendsTalk', meta: { requireAuth: true },
			components: {
				follower: followerCard,
				following: followingCard,
				friendInfo: friendInfoCard,
				talkBox: talkBoxCard,
				default: friendInfoCard,
			}
		}, {
			path: 'find', name: 'friendsFind', meta: { requireauth: true },
			components: {
				follower: followerCard,
				following: followingCard,
				friendInfo: friendFinderCard,
				initBox: initBoxCard,
				talkBox: talkBoxCard,
				default: friendInfoCard,
			}
		}, {
			path: 'setter', name: 'friendsSetter', meta: { requireauth: true },
			components: {
			}
		}, {
			path: 'makePaty', name: 'friendsMakePaty', meta: { requireauth: true },
			components: {
			}
		}]
	}]
}

export default homeRouter
