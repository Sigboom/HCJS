const Header = ()=>import('@/components/public/Header')
const Footer = ()=>import('@/components/public/Footer')
const KnowNet = ()=>import('@/components/knowNet/KnowNet')
const knowNetView = ()=>import('@/components/knowNet/views/knowNet')
const userMenuCard = ()=>import('@/components/home/cards/userMenu')

const knowNetRouter = {
	path: '/knowNet',
	components: {
		header: Header,
		main: KnowNet,
		footer: Footer,
		default: KnowNet,
	},
	children: [{
		path: '',
		components: {
			menu: userMenuCard,
			views: knowNetView,
			default: knowNetView,
		},
		children: [{
			path: '', name: 'knowNetDefault', meta: { requireAuth: true },
			components: {
			}
		}]
	}]
}

export default knowNetRouter
