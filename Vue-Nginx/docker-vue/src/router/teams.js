const Header = ()=>import('@/components/public/Header')
const Footer = ()=>import('@/components/public/Footer')
const Teams = ()=>import('@/components/teams/Teams')
const teamsView = ()=>import('@/components/teams/views/teams')
const teamMakerView = ()=>import('@/components/teams/views/teamMaker')
const teamsSetterView = ()=>import('@/components/teams/views/teamsSetter')
const userMenuCard = ()=>import('@/components/home/cards/userMenu')
const followerCard = ()=>import('@/components/teams/cards/follower')
const followingCard = ()=>import('@/components/teams/cards/following')
const teamMenuCard = ()=>import('@/components/teams/cards/teamMenu')
const initBoxCard = ()=>import('@/components/teams/cards/initBox')
const teamBoxCard = ()=>import('@/components/teams/cards/teamBox')
const teamSetterCard = ()=>import('@/components/teams/cards/teamSetter')

const teamRouter = {
	path: '/teams',
	components: {
		header: Header,
		main: Teams,
		footer: Footer,
		default: Teams,
	},
	children: [{
		path: '',
		components: {
			menu: userMenuCard,
			views: teamsView,
			default: teamsView,
		},
		children: [{
			path: '', name: 'teamDefault', meta: { requireAuth: true },
			components: {
				teamMenu: teamMenuCard,
				initBox: initBoxCard,
				teamBox: teamBoxCard,
				default: teamBoxCard,
			}
		}]
	}, {
		path: 'worker',
		components: {
			menu: userMenuCard,
			views: teamsView,
			default: teamsView,
		},
		children: [{
			path: '', name: 'teamWorker', meta: { requireAuth: true },
			components: {
				teamMenu: teamMenuCard,
				initBox: initBoxCard,
				teamBox: teamBoxCard,
				default: teamBoxCard,
			}
		}]
	}, {
		path: 'maker',
		components: {
			menu: userMenuCard,
			views: teamMakerView,
			default: teamMakerView,
		},
		children: [{
			path: '', name: 'teamMaker', meta: { requireAuth: true },
			components: {
				follower: followerCard,
				following: followingCard,
			}

		}]
	}, {
		path: 'setter',
		components: {
			menu: userMenuCard,
			views: teamsSetterView,
			default: teamsSetterView,
		},
		children: [{
			path: '', name: 'teamsSetter', meta: { requireAuth: true },
			components: {
				teamMenu: teamMenuCard,
				teamBox: teamSetterCard,
				default: teamSetterCard,
			}
		}]
	}]
}

export default teamRouter
