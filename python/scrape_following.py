from bs4 import BeautifulSoup


def scrape_following(html: str):
	soup = BeautifulSoup(html, 'html.parser')

	matches = soup.find_all('p', id=lambda x: x and x.startswith('card-title-spotify:user')) # type: ignore

	print(matches)
	titles = [tag['title'] for tag in matches] # type: ignore
	ids = [tag['id'].removeprefix('card-title-spotify:user:')[:-2] for tag in matches] # type: ignore
	print(titles)
	print(ids)

scrape_following('''<html lang="en-GB" dir="ltr" class="no-focus-outline spotify__os--is-macos spotify__container--is-web">

<head>
	<meta http-equiv="origin-trial"
		content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==">
	<meta charset="utf-8">
	<title>Spotify – nzgative</title>
	<meta property="og:site_name" content="Spotify">
	<meta property="fb:app_id" content="174829003346">
	<link rel="icon" sizes="32x32" type="image/png" href="https://open.spotifycdn.com/cdn/images/favicon32.b64ecc03.png">
	<link rel="icon" sizes="16x16" type="image/png" href="https://open.spotifycdn.com/cdn/images/favicon16.1c487bff.png">
	<link rel="icon" href="https://open.spotifycdn.com/cdn/images/favicon.0f31d2ea.ico">
	<meta http-equiv="X-UA-Compatible" content="IE=9">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
	<link rel="preload" href="https://encore.scdn.co/fonts/SpotifyMixUI-Regular-cc3b1de388efa4cbca6c75cebc24585e.woff2"
		as="font" type="font/woff2" crossorigin="anonymous">
	<link rel="preload"
		href="https://encore.scdn.co/fonts/SpotifyMixUITitleVariable-8769ccfde3379b7ebcadd9529b49d0cc.woff2" as="font"
		type="font/woff2" crossorigin="anonymous">
	<link rel="preload" href="https://encore.scdn.co/fonts/SpotifyMixUI-Bold-4264b799009b1db5c491778b1bc8e5b7.woff2"
		as="font" type="font/woff2" crossorigin="anonymous">
	<link rel="preload"
		href="https://encore.scdn.co/fonts/SpotifyMixUITitleVariable-8769ccfde3379b7ebcadd9529b49d0cc.woff2" as="font"
		type="font/woff2" crossorigin="anonymous">
	<meta property="og:title" content="nzgative">
	<meta property="og:description" content="User · nzgative">
	<meta property="og:url" content="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu">
	<meta property="og:type" content="profile">
	<meta property="og:site_name" content="Spotify">
	<meta property="og:image" content="https://i.scdn.co/image/ab6775700000ee8556f631bbdd9d39ac92b401a4">
	<meta name="description" content="User · nzgative">
	<meta name="google" content="notranslate">
	<meta name="al:android:app_name" content="Spotify">
	<meta name="al:android:package" content="com.spotify.music">
	<meta name="al:android:url"
		content="spotify://user/kw1zwmvfczcvnf03b9h3rxnzu/?flow_ctx=48674279-dca0-467a-a863-77ef24a3d14a%3A1747729155">
	<meta name="al:ios:app_name" content="Spotify">
	<meta name="al:ios:app_store_id" content="324684580">
	<meta name="al:ios:url"
		content="spotify://user/kw1zwmvfczcvnf03b9h3rxnzu/?flow_ctx=48674279-dca0-467a-a863-77ef24a3d14a%3A1747729155">
	<meta name="twitter:site" content="@spotify">
	<meta name="twitter:title" content="nzgative">
	<meta name="twitter:description" content="User · nzgative">
	<meta name="twitter:image" content="https://i.scdn.co/image/ab6775700000ee8556f631bbdd9d39ac92b401a4">
	<meta name="twitter:card" content="summary">
	<link rel="canonical" href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu">
	<link rel="alternate" href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" hreflang="x-default">
	<link rel="alternate" href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" hreflang="en">
	<link rel="alternate"
		href="android-app://com.spotify.music/spotify/user/kw1zwmvfczcvnf03b9h3rxnzu?flow_ctx=48674279-dca0-467a-a863-77ef24a3d14a%3A1747729155">
	<link rel="manifest" href="https://open.spotifycdn.com/cdn/generated/manifest-web-player.1609946b.json">
	<style data-styled="active"></style>
	<style data-styled="active" data-styled-version="5.3.11"></style>
	<link rel="stylesheet" href="https://open.spotifycdn.com/cdn/build/web-player/web-player.c1609bfd.css">
	<link rel="preconnect" href="https://apresolve.spotify.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://clienttoken.spotify.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://api-partner.spotify.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://spclient.wg.spotify.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://api.spotify.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://daily-mix.scdn.co" crossorigin="anonymous">
	<link rel="preconnect" href="https://exp.wg.spotify.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://i.scdn.co" crossorigin="anonymous">
	<link rel="preconnect" href="https://lineup-images.scdn.co" crossorigin="anonymous">
	<link rel="preconnect" href="https://mosaic.scdn.co" crossorigin="anonymous">
	<link rel="preconnect" href="https://open.spotifycdn.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://open-exp.spotifycdn.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://pixel-static.spotify.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://pixel.spotify.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://pl.scdn.co" crossorigin="anonymous">
	<link rel="preconnect" href="https://guc3-dealer.spotify.com" crossorigin="anonymous">
	<link rel="preconnect" href="https://guc3-spclient.spotify.com" crossorigin="anonymous">
	<link rel="preload" href="https://open.spotifycdn.com/cdn/generated-locales/web-player/en-GB.b395312b.json"
		data-translations-url-for-locale="en-GB" as="fetch" crossorigin="anonymous" type="application/json">
	<style>
		.grecaptcha-badge {
			display: none !important;
		}
	</style>
	<style id="_goober">
		.go1475592160 {
			height: 0;
		}

		.go1671063245 {
			height: auto;
		}

		.go1888806478 {
			display: flex;
			flex-wrap: wrap;
			flex-grow: 1;
		}

		@media (min-width:600px) {
			.go1888806478 {
				flex-grow: initial;
				min-width: 288px;
			}
		}

		.go167266335 {
			background-color: #313131;
			font-size: 0.875rem;
			line-height: 1.43;
			letter-spacing: 0.01071em;
			color: #fff;
			align-items: center;
			padding: 6px 16px;
			border-radius: 4px;
			box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 0px 1px 18px 0px rgba(0, 0, 0, 0.12);
		}

		.go3162094071 {
			padding-left: 20px;
		}

		.go3844575157 {
			background-color: #313131;
		}

		.go1725278324 {
			background-color: #43a047;
		}

		.go3651055292 {
			background-color: #d32f2f;
		}

		.go4215275574 {
			background-color: #ff9800;
		}

		.go1930647212 {
			background-color: #2196f3;
		}

		.go946087465 {
			display: flex;
			align-items: center;
			padding: 8px 0;
		}

		.go703367398 {
			display: flex;
			align-items: center;
			margin-left: auto;
			padding-left: 16px;
			margin-right: -8px;
		}

		.go3963613292 {
			width: 100%;
			position: relative;
			transform: translateX(0);
			top: 0;
			right: 0;
			bottom: 0;
			left: 0;
			min-width: 288px;
		}

		.go1141946668 {
			box-sizing: border-box;
			display: flex;
			max-height: 100%;
			position: fixed;
			z-index: 1400;
			height: auto;
			width: auto;
			transition: top 300ms ease 0ms, right 300ms ease 0ms, bottom 300ms ease 0ms, left 300ms ease 0ms, max-width 300ms ease 0ms;
			pointer-events: none;
			max-width: calc(100% - 40px);
		}

		.go1141946668 .notistack-CollapseWrapper {
			padding: 6px 0px;
			transition: padding 300ms ease 0ms;
		}

		@media (max-width:599.95px) {
			.go1141946668 {
				width: 100%;
				max-width: calc(100% - 32px);
			}
		}

		.go3868796639 .notistack-CollapseWrapper {
			padding: 2px 0px;
		}

		.go3118922589 {
			top: 14px;
			flex-direction: column;
		}

		.go1453831412 {
			bottom: 14px;
			flex-direction: column-reverse;
		}

		.go4027089540 {
			left: 20px;
		}

		@media (min-width:600px) {
			.go4027089540 {
				align-items: flex-start;
			}
		}

		@media (max-width:599.95px) {
			.go4027089540 {
				left: 16px;
			}
		}

		.go2989568495 {
			right: 20px;
		}

		@media (min-width:600px) {
			.go2989568495 {
				align-items: flex-end;
			}
		}

		@media (max-width:599.95px) {
			.go2989568495 {
				right: 16px;
			}
		}

		.go4034260886 {
			left: 50%;
			transform: translateX(-50%);
		}

		@media (min-width:600px) {
			.go4034260886 {
				align-items: center;
			}
		}
	</style>
	<link rel="prefetch" as="style"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-page-error-template.9420c935.css">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-page-error-template.9420c935.js">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/4245.9adf2d07.js">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/1222.a5ee19f9.js">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/8463.2948183c.js">
	<link rel="prefetch" as="style"
		href="https://open.spotifycdn.com/cdn/build/web-player/xpui-routes-search.61dfe8b0.css">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/xpui-routes-search.61dfe8b0.js">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/3858.272d6a82.js">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/5837.ec9e864b.js">
	<link rel="prefetch" as="style" href="https://open.spotifycdn.com/cdn/build/web-player/home-hpto.e2207eda.css">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/home-hpto.e2207eda.js">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/home-ads-container.07ac790d.js">
	<link rel="prefetch" as="style"
		href="https://open.spotifycdn.com/cdn/build/web-player/xpui-routes-offline-browse.5adfcf20.css">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/xpui-routes-offline-browse.5adfcf20.js">
	<link rel="prefetch" as="style"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-offline-empty-state.e2fecc9f.css">
	<link charset="utf-8" rel="prefetch" as="script"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-offline-empty-state.e2fecc9f.js">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-feedback-bar.15e8ecbd.css">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/xpui-routes-your-library-x.101293c5.css">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-now-playing-bar.e974062c.css">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-top-bar.efd06566.css">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/xpui-routes-profile.6ee95f2b.css">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-video-player.d358279c.css">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-leaderboard-component.a43825a1.css">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-panel-section.864a10d2.css">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/xpui-root-dialogs.a595cc12.css">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-watch-feed-view-container.06fb8d17.css">
	<link rel="stylesheet" type="text/css"
		href="https://open.spotifycdn.com/cdn/build/web-player/dwp-user-comments.8ad92f2d.css">
</head>

<body class="encore-dark-theme encore-layout-themes">
	<div class="body-drag-top"></div>
	<div style="">
		<div class="grecaptcha-badge" data-style="bottomright"
			style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;">
			<div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation"
					name="a-u3pcvh31jcw7" frameborder="0" scrolling="no"
					sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation"
					src="https://www.google.com/recaptcha/enterprise/anchor?ar=1&amp;k=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39&amp;co=aHR0cHM6Ly9vcGVuLnNwb3RpZnkuY29tOjQ0Mw..&amp;hl=en&amp;v=jt8Oh2-Ue1u7nEbJQUIdocyd&amp;size=invisible&amp;cb=kyih5lrndqvr"></iframe>
			</div>
			<div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response"
				class="g-recaptcha-response"
				style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea>
		</div><iframe style="display: none;"></iframe>
	</div>
	<div id="ad-tracking-pixel" style="display: none;"></div>
	<div id="main">
		<div data-testid="root" class="Root global-nav centered-layout" style="--panel-gap: 8px; --zoom-level: 100;">
			<div></div>
			<div class="ZQftYELq0aOsg6tPbVbV" data-right-sidebar-hidden="false">
				<div class="wp7mZFPzV7Qmo51F0NA_ pKJyyZ_7ei9TgOxrTFHX axu7kRtHOzwIb8b14FT6 searchInputCollapsed"
					id="global-nav-bar" data-testid="global-nav-bar">
					<div class="pIM9jg__39NIpOvXG89b"><a class="nmAHq8nfXRtoQmKU1gaF" href="/"><svg role="img" viewBox="0 0 24 24"
								class="e-9911-logo e-9911-baseline" aria-label="Spotify" aria-hidden="false" height="32"
								data-encore-id="logoSpotify" style="--encore-logo-fill-color: var(--decorative-base);">
								<title>Spotify</title>
								<path
									d="M13.427.01C6.805-.253 1.224 4.902.961 11.524.698 18.147 5.853 23.728 12.476 23.99c6.622.263 12.203-4.892 12.466-11.514S20.049.272 13.427.01m5.066 17.579a.717.717 0 0 1-.977.268 14.4 14.4 0 0 0-5.138-1.747 14.4 14.4 0 0 0-5.42.263.717.717 0 0 1-.338-1.392c1.95-.474 3.955-.571 5.958-.29 2.003.282 3.903.928 5.647 1.92a.717.717 0 0 1 .268.978m1.577-3.15a.93.93 0 0 1-1.262.376 17.7 17.7 0 0 0-5.972-1.96 17.7 17.7 0 0 0-6.281.238.93.93 0 0 1-1.11-.71.93.93 0 0 1 .71-1.11 19.5 19.5 0 0 1 6.94-.262 19.5 19.5 0 0 1 6.599 2.165c.452.245.62.81.376 1.263m1.748-3.551a1.147 1.147 0 0 1-1.546.488 21.4 21.4 0 0 0-6.918-2.208 21.4 21.4 0 0 0-7.259.215 1.146 1.146 0 0 1-.456-2.246 23.7 23.7 0 0 1 8.034-.24 23.7 23.7 0 0 1 7.657 2.445c.561.292.78.984.488 1.546m13.612-.036-.832-.247c-1.67-.495-2.14-.681-2.14-1.353 0-.637.708-1.327 2.264-1.327 1.539 0 2.839.752 3.51 1.31.116.096.24.052.24-.098V6.935c0-.097-.027-.15-.098-.203-.83-.62-2.272-1.07-3.723-1.07-2.953 0-4.722 1.68-4.722 3.59 0 2.157 1.371 2.91 3.626 3.546l.973.274c1.689.478 1.998.902 1.998 1.556 0 1.097-.831 1.433-2.07 1.433-1.556 0-3.457-.911-4.35-2.025-.08-.098-.177-.053-.177.062v2.423c0 .097.01.141.08.22.743.814 2.52 1.53 4.59 1.53 2.546 0 4.456-1.485 4.456-3.784 0-1.787-1.052-2.865-3.625-3.635m10.107-1.76c-1.68 0-2.653 1.026-3.219 2.052V9.376c0-.08-.044-.124-.124-.124h-2.22c-.079 0-.123.044-.123.124V20.72c0 .08.044.124.124.124h2.22c.079 0 .123-.044.123-.124v-4.536c.566 1.025 1.521 2.034 3.237 2.034 2.264 0 3.89-1.955 3.89-4.581s-1.644-4.545-3.908-4.545m-.654 6.986c-1.185 0-2.211-1.167-2.618-2.458.407-1.362 1.344-2.405 2.618-2.405 1.211 0 2.051.92 2.051 2.423s-.84 2.44-2.051 2.44m40.633-6.826h-2.264c-.08 0-.115.017-.15.097l-2.282 5.483-2.29-5.483c-.035-.08-.07-.097-.15-.097h-3.661v-.584c0-.955.645-1.397 1.476-1.397.496 0 1.035.256 1.415.486.089.053.15-.008.115-.088l-.796-1.901a.26.26 0 0 0-.124-.133c-.389-.203-1.025-.38-1.644-.38-1.875 0-2.954 1.432-2.954 3.254v.743h-1.503c-.08 0-.124.044-.124.124v1.768c0 .08.044.124.124.124h1.503v6.668c0 .08.044.123.124.123h2.264c.08 0 .124-.044.124-.123v-6.668h1.936l2.812 6.11-1.512 3.325c-.044.098.009.142.097.142h2.414c.08 0 .116-.018.15-.097l4.997-11.355c.035-.08-.009-.141-.097-.141M54.964 9.04c-2.865 0-4.837 2.025-4.837 4.616 0 2.573 1.971 4.616 4.837 4.616 2.856 0 4.846-2.043 4.846-4.616 0-2.591-1.99-4.616-4.846-4.616m.008 7.065c-1.37 0-2.343-1.043-2.343-2.45 0-1.405.973-2.449 2.343-2.449 1.362 0 2.335 1.043 2.335 2.45 0 1.406-.973 2.45-2.335 2.45m33.541-6.334a1.24 1.24 0 0 0-.483-.471 1.4 1.4 0 0 0-.693-.17q-.384 0-.693.17a1.24 1.24 0 0 0-.484.471q-.174.302-.174.681 0 .375.174.677.175.3.484.471t.693.17.693-.17.483-.471.175-.676q0-.38-.175-.682m-.211 1.247a1 1 0 0 1-.394.39 1.15 1.15 0 0 1-.571.14 1.16 1.16 0 0 1-.576-.14 1 1 0 0 1-.391-.39 1.14 1.14 0 0 1-.14-.566q0-.316.14-.562t.391-.388.576-.14q.32 0 .57.14.253.141.395.39t.142.565q0 .312-.142.56m-19.835-5.78c-.85 0-1.468.6-1.468 1.396s.619 1.397 1.468 1.397c.866 0 1.485-.6 1.485-1.397 0-.796-.619-1.397-1.485-1.397m19.329 5.19a.31.31 0 0 0 .134-.262q0-.168-.132-.266-.132-.099-.381-.099h-.588v1.229h.284v-.489h.154l.374.489h.35l-.41-.518a.5.5 0 0 0 .215-.084m-.424-.109h-.26v-.3h.27q.12 0 .184.036a.12.12 0 0 1 .065.116.12.12 0 0 1-.067.111.4.4 0 0 1-.192.037M69.607 9.252h-2.263c-.08 0-.124.044-.124.124v8.56c0 .08.044.123.124.123h2.263c.08 0 .124-.044.124-.123v-8.56c0-.08-.044-.124-.124-.124m-3.333 6.605a2.1 2.1 0 0 1-1.053.257c-.725 0-1.185-.425-1.185-1.362v-3.484h2.211c.08 0 .124-.044.124-.124V9.376c0-.08-.044-.124-.124-.124h-2.21V6.944c0-.097-.063-.15-.15-.08l-3.954 3.113c-.053.044-.07.088-.07.16v1.007c0 .08.044.124.123.124h1.539v3.855c0 2.087 1.203 3.06 2.918 3.06.743 0 1.46-.194 1.884-.442.062-.035.07-.07.07-.133v-1.68c0-.088-.044-.115-.123-.07"
									transform="translate(-0.95,0)"></path>
							</svg></a></div>
					<div class="gj5VcIUC9oD2p4BsxzGE">
						<div class="lj0eGI6WEtfxFX7irC03"><button data-testid="home-button"
								class="Button-sc-1dqy6lx-0 LlNsd e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only Dp3xccI7c2f_JSJ8OHYu obd_bH64Snp1npdw29XM VUXMMFKWudUWE1kIXZoS"
								aria-label="Home" data-encore-id="buttonTertiary"><span aria-hidden="true"
									class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
										class="e-9911-icon e-9911-baseline" viewBox="0 0 24 24">
										<path
											d="M12.5 3.247a1 1 0 0 0-1 0L4 7.577V20h4.5v-6a1 1 0 0 1 1-1h5a1 1 0 0 1 1 1v6H20V7.577l-7.5-4.33zm-2-1.732a3 3 0 0 1 3 0l7.5 4.33a2 2 0 0 1 1 1.732V21a1 1 0 0 1-1 1h-6.5a1 1 0 0 1-1-1v-6h-3v6a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V7.577a2 2 0 0 1 1-1.732l7.5-4.33z">
										</path>
									</svg></span></button>
							<div class="_b3hhmbWtOY8_1M1mM1H">
								<form
									class="e-9911-form-input-icon e-9911-baseline e-9911-form-input-icon--leading e-9911-form-input-icon--trailing b7r2WRiu5f9Q99qmyreh"
									role="search" data-encore-id="formInputIcon"
									style="--encore-form-input-icon-padding-leading: calc(24px + var(--encore-spacing-tighter, 12px) * 2); --encore-form-input-icon-padding-trailing: calc(24px + var(--encore-spacing-tighter, 12px) * 2);">
									<div class="e-9911-form-input-icon__icon e-9911-form-input-icon__icon--leading">
										<div><button
												class="Button-sc-1dqy6lx-0 imSSKJ e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only e-9911-button-tertiary--condensed EJttP30F1zYHeAw7ISHb"
												aria-label="Search" data-encore-id="buttonTertiary"><span aria-hidden="true"
													class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
														class="e-9911-icon e-9911-baseline" viewBox="0 0 24 24">
														<path
															d="M10.533 1.27893C5.35215 1.27893 1.12598 5.41887 1.12598 10.5579C1.12598 15.697 5.35215 19.8369 10.533 19.8369C12.767 19.8369 14.8235 19.0671 16.4402 17.7794L20.7929 22.132C21.1834 22.5226 21.8166 22.5226 22.2071 22.132C22.5976 21.7415 22.5976 21.1083 22.2071 20.7178L17.8634 16.3741C19.1616 14.7849 19.94 12.7634 19.94 10.5579C19.94 5.41887 15.7138 1.27893 10.533 1.27893ZM3.12598 10.5579C3.12598 6.55226 6.42768 3.27893 10.533 3.27893C14.6383 3.27893 17.94 6.55226 17.94 10.5579C17.94 14.5636 14.6383 17.8369 10.533 17.8369C6.42768 17.8369 3.12598 14.5636 3.12598 10.5579Z">
														</path>
													</svg></span></button><svg data-encore-id="icon" role="img" aria-hidden="true"
												class="e-9911-icon e-9911-baseline M9l40ptEBXPm03dU3X1k" data-testid="search-icon"
												viewBox="0 0 24 24"
												style="--encore-icon-height: var(--encore-graphic-size-decorative-larger-3); --encore-icon-width: var(--encore-graphic-size-decorative-larger-3);">
												<path
													d="M10.533 1.27893C5.35215 1.27893 1.12598 5.41887 1.12598 10.5579C1.12598 15.697 5.35215 19.8369 10.533 19.8369C12.767 19.8369 14.8235 19.0671 16.4402 17.7794L20.7929 22.132C21.1834 22.5226 21.8166 22.5226 22.2071 22.132C22.5976 21.7415 22.5976 21.1083 22.2071 20.7178L17.8634 16.3741C19.1616 14.7849 19.94 12.7634 19.94 10.5579C19.94 5.41887 15.7138 1.27893 10.533 1.27893ZM3.12598 10.5579C3.12598 6.55226 6.42768 3.27893 10.533 3.27893C14.6383 3.27893 17.94 6.55226 17.94 10.5579C17.94 14.5636 14.6383 17.8369 10.533 17.8369C6.42768 17.8369 3.12598 14.5636 3.12598 10.5579Z">
												</path>
											</svg></div>
									</div>
									<div class="ODl7TwNawIfBwiZv1Czg"><input
											class="e-9911-form-input e-9911-baseline e-9911-form-control encore-text-body-medium CVuGEUIxLkNKpMds8AFS R69APjfNV0o9tAbfrWZf"
											data-encore-id="formInput" role="combobox" aria-owns="recent-searches-dropdown"
											aria-controls="recent-searches-dropdown" aria-expanded="true" data-testid="search-input"
											aria-label="What do you want to play?" data-top-bar-search="true" type="search" spellcheck="false"
											placeholder="What do you want to play?" tabindex="-1">
										<div class="dM_TEJo05MxBvrLzfNrW" aria-hidden="true"><span class="upGmCR5y3yDImbt6sHOl">What do you
												want to play?</span><span class="IYex0sXu8fnCz1FqFbRe"><kbd
													class="e-9911-text encore-text-body-medium xlLQHgpip3xYOwRYpwun"
													data-encore-id="text">⌘</kbd><kbd
													class="e-9911-text encore-text-body-medium xlLQHgpip3xYOwRYpwun"
													data-encore-id="text">K</kbd></span></div>
									</div>
									<div class="e-9911-form-input-icon__icon e-9911-form-input-icon__icon--trailing"><button
											data-testid="clear-button"
											class="Button-sc-1dqy6lx-0 iBjBCb e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only e-9911-button-tertiary--condensed MdMAXXFPalD99eigsBug"
											aria-label="Clear search field" data-encore-id="buttonTertiary"><span aria-hidden="true"
												class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
													class="e-9911-icon e-9911-baseline" viewBox="0 0 24 24">
													<path
														d="M3.293 3.293a1 1 0 0 1 1.414 0L12 10.586l7.293-7.293a1 1 0 1 1 1.414 1.414L13.414 12l7.293 7.293a1 1 0 0 1-1.414 1.414L12 13.414l-7.293 7.293a1 1 0 0 1-1.414-1.414L10.586 12 3.293 4.707a1 1 0 0 1 0-1.414z">
													</path>
												</svg></span></button>
										<div class="BV0jjn_h5TtMMl8YKuZ0"><button data-testid="browse-button"
												class="Button-sc-1dqy6lx-0 iBjBCb e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only e-9911-button-tertiary--condensed"
												aria-label="Browse" data-encore-id="buttonTertiary"><span aria-hidden="true"
													class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
														class="e-9911-icon e-9911-baseline" viewBox="0 0 24 24">
														<path d="M15 15.5c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2z"></path>
														<path
															d="M1.513 9.37A1 1 0 0 1 2.291 9h19.418a1 1 0 0 1 .979 1.208l-2.339 11a1 1 0 0 1-.978.792H4.63a1 1 0 0 1-.978-.792l-2.339-11a1 1 0 0 1 .201-.837zM3.525 11l1.913 9h13.123l1.913-9H3.525zM4 2a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v4h-2V3H6v3H4V2z">
														</path>
													</svg></span></button></div>
									</div>
								</form>
							</div>
						</div>
					</div>
					<div class="N9r2VuXMBlhRSVF5dCek">
						<div class="VUXMMFKWudUWE1kIXZoS rwdnt1SmeRC_lhLVfIzg"><a draggable="false"
								class="Button-sc-1dqy6lx-0 dzIYeQ encore-text-body-small-bold e-9911-overflow-wrap-anywhere e-9911-button--small e-9911-button--leading"
								data-encore-id="buttonTertiary" href="/download"><span aria-hidden="true"
									class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
										class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
										style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
										<path
											d="M4.995 8.745a.75.75 0 0 1 1.06 0L7.25 9.939V4a.75.75 0 0 1 1.5 0v5.94l1.195-1.195a.75.75 0 1 1 1.06 1.06L8 12.811l-.528-.528a.945.945 0 0 1-.005-.005L4.995 9.805a.75.75 0 0 1 0-1.06z">
										</path>
										<path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13z"></path>
									</svg></span><span class="e-9911-text encore-text-body-small-bold ellipsis-one-line"
									data-encore-id="text">Install App</span></a>
							<div class="LedDBMWCxYhMD20KtPJo NPvLJSRWfv1Joo8dF0D8"><button data-testid="whats-new-feed-button"
									class="Button-sc-1dqy6lx-0 giZtyl encore-text-body-small-bold e-9911-overflow-wrap-anywhere e-9911-button-tertiary--condensed WtC1lGbmQRplD6JBhNFU"
									aria-label="What’s New" data-encore-id="buttonTertiary"><svg data-encore-id="icon" role="img"
										aria-hidden="true" class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
										style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
										<path
											d="M8 1.5a4 4 0 0 0-4 4v3.27a.75.75 0 0 1-.1.373L2.255 12h11.49L12.1 9.142a.75.75 0 0 1-.1-.374V5.5a4 4 0 0 0-4-4zm-5.5 4a5.5 5.5 0 0 1 11 0v3.067l2.193 3.809a.75.75 0 0 1-.65 1.124H10.5a2.5 2.5 0 0 1-5 0H.957a.75.75 0 0 1-.65-1.124L2.5 8.569V5.5zm4.5 8a1 1 0 1 0 2 0H7z">
										</path>
									</svg></button><button data-testid="friend-activity-button" data-restore-focus-key="buddy_feed"
									class="Button-sc-1dqy6lx-0 giZtyl encore-text-body-small-bold e-9911-overflow-wrap-anywhere e-9911-button-tertiary--condensed WtC1lGbmQRplD6JBhNFU"
									aria-label="Friend Activity" data-encore-id="buttonTertiary"><svg data-encore-id="icon" role="img"
										aria-hidden="true" class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
										style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
										<path
											d="M3.849 10.034c-.021-.465.026-.93.139-1.381H1.669c.143-.303.375-.556.665-.724l.922-.532a1.631 1.631 0 0 0 .436-2.458 1.809 1.809 0 0 1-.474-1.081c-.01-.19.01-.38.057-.563a1.123 1.123 0 0 1 .627-.7 1.2 1.2 0 0 1 .944 0c.149.065.282.161.392.281.108.12.188.263.237.417.049.183.068.372.057.561a1.81 1.81 0 0 1-.475 1.084 1.6 1.6 0 0 0-.124 1.9c.36-.388.792-.702 1.272-.927v-.015c.48-.546.768-1.233.821-1.958a3.23 3.23 0 0 0-.135-1.132 2.657 2.657 0 0 0-5.04 0c-.111.367-.157.75-.135 1.133.053.724.341 1.41.821 1.955A.126.126 0 0 1 2.565 6a.13.13 0 0 1-.063.091l-.922.532A3.2 3.2 0 0 0-.004 9.396v.75h3.866c.001-.033-.01-.071-.013-.112zm10.568-3.4-.922-.532a.132.132 0 0 1-.064-.091.12.12 0 0 1 .028-.1c.48-.546.768-1.233.821-1.958a3.289 3.289 0 0 0-.135-1.135A2.635 2.635 0 0 0 12.7 1.233a2.669 2.669 0 0 0-3.042.64 2.646 2.646 0 0 0-.554.948c-.11.367-.156.75-.134 1.133.053.724.341 1.41.821 1.955.005.006 0 .011 0 .018.48.225.911.54 1.272.927a1.6 1.6 0 0 0-.125-1.907 1.809 1.809 0 0 1-.474-1.081c-.01-.19.009-.38.057-.563a1.123 1.123 0 0 1 .627-.7 1.2 1.2 0 0 1 .944 0c.149.065.282.161.392.281.107.12.187.26.236.413.05.184.07.375.058.565a1.81 1.81 0 0 1-.475 1.084 1.633 1.633 0 0 0 .438 2.456l.922.532c.29.169.52.421.664.724h-2.319c.113.452.16.918.139 1.383 0 .04-.013.078-.017.117h3.866v-.75a3.2 3.2 0 0 0-1.58-2.778v.004zm-3.625 6-.922-.532a.13.13 0 0 1-.061-.144.122.122 0 0 1 .025-.047 3.33 3.33 0 0 0 .821-1.958 3.229 3.229 0 0 0-.135-1.132 2.657 2.657 0 0 0-5.041 0c-.11.367-.156.75-.134 1.133.053.724.341 1.41.821 1.955a.127.127 0 0 1 .028.106.128.128 0 0 1-.063.091l-.922.532a3.2 3.2 0 0 0-1.584 2.773v.75h8.75v-.75a3.2 3.2 0 0 0-1.583-2.781v.004zm-5.5 2.023c.143-.303.375-.556.665-.724l.922-.532a1.63 1.63 0 0 0 .436-2.458 1.809 1.809 0 0 1-.474-1.081c-.01-.19.009-.38.057-.563a1.123 1.123 0 0 1 .627-.7 1.2 1.2 0 0 1 .944 0c.149.065.282.161.392.281.108.12.188.263.237.417.049.183.068.372.057.561a1.81 1.81 0 0 1-.475 1.084 1.632 1.632 0 0 0 .438 2.456l.922.532c.29.169.52.421.664.724l-5.412.003z">
										</path>
									</svg></button></div><button data-testid="user-widget-link" aria-expanded="false"
								class="Button-sc-1dqy6lx-0 iFsPEJ encore-text-body-medium-bold e-9911-overflow-wrap-anywhere e-9911-button-tertiary--condensed KAq2kDjXj2VS4eXrFL4i"
								aria-label="lucas" data-encore-id="buttonTertiary"
								style="background-color: var(--background-elevated-base);"><span
									class="e-9911-text encore-text-body-small-bold LKfKy7bXKmlkMEANVJMS" data-encore-id="text"
									data-testid="username-first-letter"
									style="background-color: rgb(80, 155, 245); color: rgb(0, 0, 0); line-height: 32px;">L</span></button>
						</div>
					</div>
				</div>
				<div class="oDWO4yGAZ2kZlt3TTS4E" style="--left-sidebar-width: 72;"></div>
				<div id="Desktop_LeftSidebar_Id" class="BdcvqBAid96FaHAmPYw_" style="--left-sidebar-width: 72;">
					<nav class="lYpiKR_qEjl1jGGyEvsA" aria-label="Main">
						<div class="lHJd4oSttKLxkxuoZ0Lr wM72343CksOCaL3bZvKK">
							<div class="hgJel0bLlS_1Uf0EIfSA YourLibraryX sikBfynL1Y6I25nVpbAg" tabindex="-1"
								style="--placeholder-image: url(https://open.spotifycdn.com/cdn/images/ylx-row-placeholder.ea7b0f5d.webp); --placeholder-artist-image: url(https://open.spotifycdn.com/cdn/images/ylx-artist-row-placeholder.4521609f.webp); --placeholder-compact-image: url(https://open.spotifycdn.com/cdn/images/ylx-compact-row-placeholder.9a165ac8.webp);">
								<div class="">
									<header class="HjPqU_UW2egr14mRSom9 oZT8iKL42zhLAm_zE5F5">
										<div class="tAfozCQs48q1JYdphYXi iYP0xuQiJCgi7gx1jUPJ">
											<div class="FTiXRW7kAldHmLaxVQ2N iYP0xuQiJCgi7gx1jUPJ">
												<div class="bDHk5k9wfICYjDSC27zp WHTLfjA4oq5AQak5E8CQ"><button type="button"
														aria-label="Open Your Library"
														class="oaVwShR89gQxLH2tco5G NxEINIJHGytq4gF1r2N1 or84FBarW2zQhXfB9VFb odS2IW9wfNVHhkhc0l_X O0AN8Ty_Cxd4iLwyKATB wQnUXn1m6Gy4PH8jhslb CU0fvofmxUbTupSDNOQ3 D8wJ9TPfJzLeLJYxnad2 oE8LAmRhbeQqsZrQo4lb zWWLnqWslTLHwq3wBgGB XNjgtSbyhshr7YQcVvry mhuhir0ikRqXAPHU8ZZ1"><span
															class="Gj4v3278oIywygaUyBbt"><svg data-encore-id="icon" role="img" aria-hidden="true"
																class="e-9911-icon e-9911-baseline" viewBox="0 0 24 24">
																<path
																	d="M14.5 2.134a1 1 0 0 1 1 0l6 3.464a1 1 0 0 1 .5.866V21a1 1 0 0 1-1 1h-6a1 1 0 0 1-1-1V3a1 1 0 0 1 .5-.866zM16 4.732V20h4V7.041l-4-2.309zM3 22a1 1 0 0 1-1-1V3a1 1 0 0 1 2 0v18a1 1 0 0 1-1 1zm6 0a1 1 0 0 1-1-1V3a1 1 0 0 1 2 0v18a1 1 0 0 1-1 1z">
																</path>
															</svg></span><span class="WJFlv_VJkA5oNs0XJMsQ"><svg data-encore-id="icon" role="img"
																aria-hidden="true" class="e-9911-icon e-9911-baseline e-9911-icon--auto-mirror"
																viewBox="0 0 24 24">
																<path
																	d="M14.457 15.207a1 1 0 0 1-1.414-1.414L14.836 12l-1.793-1.793a1 1 0 0 1 1.414-1.414l2.5 2.5a1 1 0 0 1 0 1.414l-2.5 2.5Z">
																</path>
																<path
																	d="M20 22a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h16ZM4 20V4h4v16H4Zm16 0H10V4h10v16Z">
																</path>
															</svg></span><span class="e-9911-visually-hidden" data-encore-id="visuallyHidden">
															<h1 class="e-9911-text encore-text-body-medium" data-encore-id="text">Your Library</h1>
														</span></button></div>
											</div>
											<div class="BZh0f1vbOmruyp4_t9wy QO1vC7wN5xiIjBOHGElf"><button type="button"
													class="AIlmv6h8bR5NY5R0VceT NxEINIJHGytq4gF1r2N1 or84FBarW2zQhXfB9VFb XNjgtSbyhshr7YQcVvry O0AN8Ty_Cxd4iLwyKATB D8wJ9TPfJzLeLJYxnad2 zWWLnqWslTLHwq3wBgGB l5V7KOO1aHJ4R7jYTQuV"
													aria-label="Create"><svg data-encore-id="icon" role="img" aria-hidden="true"
														class="e-9911-icon e-9911-baseline gPxvvwdrTY6FbTx3mvl1" viewBox="0 0 16 16"
														style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
														<path
															d="M15.25 8a.75.75 0 0 1-.75.75H8.75v5.75a.75.75 0 0 1-1.5 0V8.75H1.5a.75.75 0 0 1 0-1.5h5.75V1.5a.75.75 0 0 1 1.5 0v5.75h5.75a.75.75 0 0 1 .75.75z">
														</path>
													</svg></button></div>
										</div>
									</header>
								</div>
								<div data-overlayscrollbars-initialize="true" class="WxM1eb7qnneSkMiT4dvw ZjfaJlGQZ42nCWjD3FDm"
									data-overlayscrollbars="host">
									<div class="" data-overlayscrollbars-viewport="scrollbarHidden overflowXHidden overflowYScroll"
										tabindex="-1"
										style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; top: 0px; right: auto; left: 0px; width: calc(100% + 0px); padding: 0px;">
										<div class="_W_0W9Uld1vxrRfsgdQR sikBfynL1Y6I25nVpbAg">
											<div class="kCQHErMb02f7Yn3pfZzx"></div>
											<div>
												<div role="grid" aria-rowcount="14" aria-colcount="1" aria-label="Your Library" tabindex="0">
													<div class="" role="presentation">
														<div class="JUa6JJNj7R_Y3i4P8YUX" role="presentation"
															style="height: 896px; --row-height: 64px;">
															<div data-testid="top-sentinel" class="lyVkg68L7ycnwyOcO3vj" role="presentation"
																style="height: 512px;">
																<div class="eC25_w41L83mXDCqdm_A" role="row" aria-rowindex="1"
																	style="height: calc(100% - 512px);"></div>
																<div role="presentation" style="height: 512px;"></div>
															</div>
															<div role="presentation" style="transform: translateY(0px);">
																<div
																	class="NxEINIJHGytq4gF1r2N1 or84FBarW2zQhXfB9VFb odS2IW9wfNVHhkhc0l_X O0AN8Ty_Cxd4iLwyKATB XNjgtSbyhshr7YQcVvry vSC5QuwmzUhqUNWdMTJ5"
																	role="row" aria-rowindex="1" aria-selected="false" aria-setsize="14" draggable="true"
																	style="--ylx-folder-depth: 0;">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:playlist:16aI4xJPOAfN51UBlIh1BS"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:playlist:16aI4xJPOAfN51UBlIh1BS listrow-subtitle-spotify:playlist:16aI4xJPOAfN51UBlIh1BS"
																				aria-describedby="onClickHintspotify:playlist:16aI4xJPOAfN51UBlIh1BS"
																				tabindex="-1" class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:playlist:16aI4xJPOAfN51UBlIh1BS"
																				style="display: none;"></div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #80755F;"><img
																								aria-hidden="true" draggable="false" loading="eager"
																								src="https://image-cdn-ak.spotifycdn.com/image/ab67706c0000d72ce4f5e5522d24f8a73796d685"
																								data-testid="entity-image" alt=" "
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:playlist:16aI4xJPOAfN51UBlIh1BS" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK"> </span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:playlist:16aI4xJPOAfN51UBlIh1BS" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Playlist • lucas</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div
																	class="NxEINIJHGytq4gF1r2N1 or84FBarW2zQhXfB9VFb odS2IW9wfNVHhkhc0l_X O0AN8Ty_Cxd4iLwyKATB XNjgtSbyhshr7YQcVvry vSC5QuwmzUhqUNWdMTJ5"
																	role="row" aria-rowindex="2" aria-selected="false" aria-setsize="14" draggable="true"
																	style="--ylx-folder-depth: 0;">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:playlist:7vPmbWpJcdznlyj1AHIjrQ"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:playlist:7vPmbWpJcdznlyj1AHIjrQ listrow-subtitle-spotify:playlist:7vPmbWpJcdznlyj1AHIjrQ"
																				aria-describedby="onClickHintspotify:playlist:7vPmbWpJcdznlyj1AHIjrQ"
																				tabindex="-1" class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:playlist:7vPmbWpJcdznlyj1AHIjrQ"
																				style="display: none;"></div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #4378BB;">
																							<div aria-label="😛" class="Ozitxbqs1vcOukDz3GDw"><svg
																									data-encore-id="icon" role="img" aria-hidden="true"
																									class="e-9911-icon e-9911-baseline" data-testid="playlist"
																									viewBox="0 0 24 24">
																									<path
																										d="M6 3h15v15.167a3.5 3.5 0 1 1-3.5-3.5H19V5H8v13.167a3.5 3.5 0 1 1-3.5-3.5H6V3zm0 13.667H4.5a1.5 1.5 0 1 0 1.5 1.5v-1.5zm13 0h-1.5a1.5 1.5 0 1 0 1.5 1.5v-1.5z">
																									</path>
																								</svg></div>
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:playlist:7vPmbWpJcdznlyj1AHIjrQ" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">😛</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:playlist:7vPmbWpJcdznlyj1AHIjrQ" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Playlist • lucas</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div class="NxEINIJHGytq4gF1r2N1  vSC5QuwmzUhqUNWdMTJ5" role="row" aria-rowindex="3"
																	aria-selected="false" aria-setsize="14" draggable="true"
																	style="--ylx-folder-depth: 0;">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:playlist:1FkRppAGLEnEoSW9aadkgg"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:playlist:1FkRppAGLEnEoSW9aadkgg listrow-subtitle-spotify:playlist:1FkRppAGLEnEoSW9aadkgg"
																				aria-describedby="onClickHintspotify:playlist:1FkRppAGLEnEoSW9aadkgg"
																				tabindex="-1" class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:playlist:1FkRppAGLEnEoSW9aadkgg"
																				style="display: none;"></div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #304038;"><img
																								aria-hidden="true" draggable="false" loading="eager"
																								src="https://image-cdn-ak.spotifycdn.com/image/ab67706c0000d72cdc7e4d191d46316527d71224"
																								data-testid="entity-image" alt="underwater dreams"
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:playlist:1FkRppAGLEnEoSW9aadkgg" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">underwater dreams</span>
																			</p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:playlist:1FkRppAGLEnEoSW9aadkgg" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Playlist • themariasmp3</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div
																	class="NxEINIJHGytq4gF1r2N1 or84FBarW2zQhXfB9VFb odS2IW9wfNVHhkhc0l_X O0AN8Ty_Cxd4iLwyKATB XNjgtSbyhshr7YQcVvry vSC5QuwmzUhqUNWdMTJ5"
																	role="row" aria-rowindex="4" aria-selected="false" aria-setsize="14" draggable="true"
																	style="--ylx-folder-depth: 0;">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:playlist:2CUYjmhxDadq0IkffhyyMD"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:playlist:2CUYjmhxDadq0IkffhyyMD listrow-subtitle-spotify:playlist:2CUYjmhxDadq0IkffhyyMD"
																				aria-describedby="onClickHintspotify:playlist:2CUYjmhxDadq0IkffhyyMD"
																				tabindex="-1" class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:playlist:2CUYjmhxDadq0IkffhyyMD"
																				style="display: none;"></div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px;"><img aria-hidden="true"
																								draggable="false" loading="eager"
																								src="https://image-cdn-ak.spotifycdn.com/image/ab67706c0000d72cfe06e028d353e51ab0a433a2"
																								data-testid="entity-image" alt=" 🎸"
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:playlist:2CUYjmhxDadq0IkffhyyMD" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK"> 🎸</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:playlist:2CUYjmhxDadq0IkffhyyMD" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Playlist • lucas</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div class="NxEINIJHGytq4gF1r2N1  vSC5QuwmzUhqUNWdMTJ5" role="row" aria-rowindex="5"
																	aria-selected="false" aria-setsize="14" draggable="true">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:show:2KfhSm2iUeEgvYAHZyAl4T"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:show:2KfhSm2iUeEgvYAHZyAl4T listrow-subtitle-spotify:show:2KfhSm2iUeEgvYAHZyAl4T"
																				aria-describedby="onClickHintspotify:show:2KfhSm2iUeEgvYAHZyAl4T" tabindex="-1"
																				class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:show:2KfhSm2iUeEgvYAHZyAl4T" style="display: none;">
																			</div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #B80810;"><img
																								aria-hidden="true" draggable="false" loading="eager"
																								src="https://i.scdn.co/image/ab6765630000bdcfcd7cc0c30cad0e6c743a0c5d"
																								data-testid="entity-image" alt="YellowParenti "
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:show:2KfhSm2iUeEgvYAHZyAl4T" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">YellowParenti </span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:show:2KfhSm2iUeEgvYAHZyAl4T" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Podcast • Vera Lynn</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div class="NxEINIJHGytq4gF1r2N1  vSC5QuwmzUhqUNWdMTJ5" role="row" aria-rowindex="6"
																	aria-selected="false" aria-setsize="14" draggable="true">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:show:7tk1sTZDeE8p9lnxYLy4Ky"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:show:7tk1sTZDeE8p9lnxYLy4Ky listrow-subtitle-spotify:show:7tk1sTZDeE8p9lnxYLy4Ky"
																				aria-describedby="onClickHintspotify:show:7tk1sTZDeE8p9lnxYLy4Ky" tabindex="-1"
																				class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:show:7tk1sTZDeE8p9lnxYLy4Ky" style="display: none;">
																			</div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #996F20;"><img
																								aria-hidden="true" draggable="false" loading="eager"
																								src="https://i.scdn.co/image/ab6765630000bdcfafa06fb8c86aab05a7dd968b"
																								data-testid="entity-image" alt="The Deprogram"
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:show:7tk1sTZDeE8p9lnxYLy4Ky" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">The Deprogram</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:show:7tk1sTZDeE8p9lnxYLy4Ky" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Podcast • JT, Hakim, and Yugopnik</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div class="NxEINIJHGytq4gF1r2N1  vSC5QuwmzUhqUNWdMTJ5" role="row" aria-rowindex="7"
																	aria-selected="false" aria-setsize="14" draggable="true">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:show:16wUbvDT95dxzpG2KEhakK"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:show:16wUbvDT95dxzpG2KEhakK listrow-subtitle-spotify:show:16wUbvDT95dxzpG2KEhakK"
																				aria-describedby="onClickHintspotify:show:16wUbvDT95dxzpG2KEhakK" tabindex="-1"
																				class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:show:16wUbvDT95dxzpG2KEhakK" style="display: none;">
																			</div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #A46761;"><img
																								aria-hidden="true" draggable="false" loading="eager"
																								src="https://i.scdn.co/image/ab6765630000bdcf657f4372d74cdfb79fef4b55"
																								data-testid="entity-image" alt="Within Reason"
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:show:16wUbvDT95dxzpG2KEhakK" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">Within Reason</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:show:16wUbvDT95dxzpG2KEhakK" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Podcast • Alex J O'Connor</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div class="NxEINIJHGytq4gF1r2N1  vSC5QuwmzUhqUNWdMTJ5" role="row" aria-rowindex="8"
																	aria-selected="false" aria-setsize="14" draggable="true"
																	style="--ylx-folder-depth: 0;">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:playlist:0MswjXcNfHleZhRvZZkNFB"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:playlist:0MswjXcNfHleZhRvZZkNFB listrow-subtitle-spotify:playlist:0MswjXcNfHleZhRvZZkNFB"
																				aria-describedby="onClickHintspotify:playlist:0MswjXcNfHleZhRvZZkNFB"
																				tabindex="-1" class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:playlist:0MswjXcNfHleZhRvZZkNFB"
																				style="display: none;"></div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #582008;"><img
																								aria-hidden="true" draggable="false" loading="eager"
																								src="https://image-cdn-ak.spotifycdn.com/image/ab67706c0000d72c351975a4ccf1b92b580281ae"
																								data-testid="entity-image" alt="AAAAAAAAA"
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:playlist:0MswjXcNfHleZhRvZZkNFB" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">AAAAAAAAA</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:playlist:0MswjXcNfHleZhRvZZkNFB" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Playlist • jonette旎</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div class="NxEINIJHGytq4gF1r2N1  vSC5QuwmzUhqUNWdMTJ5" role="row" aria-rowindex="9"
																	aria-selected="false" aria-setsize="14" draggable="true"
																	style="--ylx-folder-depth: 0;">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:playlist:4TKBBifrUAGYG0ibftFnuy"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:playlist:4TKBBifrUAGYG0ibftFnuy listrow-subtitle-spotify:playlist:4TKBBifrUAGYG0ibftFnuy"
																				aria-describedby="onClickHintspotify:playlist:4TKBBifrUAGYG0ibftFnuy"
																				tabindex="-1" class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:playlist:4TKBBifrUAGYG0ibftFnuy"
																				style="display: none;"></div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #784840;"><img
																								aria-hidden="true" draggable="false" loading="eager"
																								src="https://image-cdn-ak.spotifycdn.com/image/ab67706c0000d72cd2157cceb28fd2a90bc7e44a"
																								data-testid="entity-image" alt="marry me if u like billie👍👍"
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:playlist:4TKBBifrUAGYG0ibftFnuy" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">marry me if u like
																					billie👍👍</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:playlist:4TKBBifrUAGYG0ibftFnuy" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Playlist • crz</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div
																	class="NxEINIJHGytq4gF1r2N1 or84FBarW2zQhXfB9VFb odS2IW9wfNVHhkhc0l_X O0AN8Ty_Cxd4iLwyKATB XNjgtSbyhshr7YQcVvry vSC5QuwmzUhqUNWdMTJ5"
																	role="row" aria-rowindex="10" aria-selected="false" aria-setsize="14" draggable="true"
																	style="--ylx-folder-depth: 0;">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:playlist:2WNMHkduIowfAMyz2IqepJ"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:playlist:2WNMHkduIowfAMyz2IqepJ listrow-subtitle-spotify:playlist:2WNMHkduIowfAMyz2IqepJ"
																				aria-describedby="onClickHintspotify:playlist:2WNMHkduIowfAMyz2IqepJ"
																				tabindex="-1" class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:playlist:2WNMHkduIowfAMyz2IqepJ"
																				style="display: none;"></div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px;"><img aria-hidden="true"
																								draggable="false" loading="eager"
																								src="https://image-cdn-ak.spotifycdn.com/image/ab67706c0000d72ce5a9928a4a16ed8d360db190"
																								data-testid="entity-image" alt="Indie Rock"
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:playlist:2WNMHkduIowfAMyz2IqepJ" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">Indie Rock</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:playlist:2WNMHkduIowfAMyz2IqepJ" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Playlist • matt_lamb</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div
																	class="NxEINIJHGytq4gF1r2N1 or84FBarW2zQhXfB9VFb odS2IW9wfNVHhkhc0l_X O0AN8Ty_Cxd4iLwyKATB XNjgtSbyhshr7YQcVvry vSC5QuwmzUhqUNWdMTJ5"
																	role="row" aria-rowindex="11" aria-selected="false" aria-setsize="14" draggable="true"
																	style="--ylx-folder-depth: 0;">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:playlist:4REUuh0eos2FS7iT87uY1P"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:playlist:4REUuh0eos2FS7iT87uY1P listrow-subtitle-spotify:playlist:4REUuh0eos2FS7iT87uY1P"
																				aria-describedby="onClickHintspotify:playlist:4REUuh0eos2FS7iT87uY1P"
																				tabindex="-1" class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:playlist:4REUuh0eos2FS7iT87uY1P"
																				style="display: none;"></div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #4858C0;">
																							<div aria-label="rao" class="Ozitxbqs1vcOukDz3GDw"><svg
																									data-encore-id="icon" role="img" aria-hidden="true"
																									class="e-9911-icon e-9911-baseline" data-testid="playlist"
																									viewBox="0 0 24 24">
																									<path
																										d="M6 3h15v15.167a3.5 3.5 0 1 1-3.5-3.5H19V5H8v13.167a3.5 3.5 0 1 1-3.5-3.5H6V3zm0 13.667H4.5a1.5 1.5 0 1 0 1.5 1.5v-1.5zm13 0h-1.5a1.5 1.5 0 1 0 1.5 1.5v-1.5z">
																									</path>
																								</svg></div>
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:playlist:4REUuh0eos2FS7iT87uY1P" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">rao</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:playlist:4REUuh0eos2FS7iT87uY1P" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Playlist • lucas</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div class="NxEINIJHGytq4gF1r2N1  vSC5QuwmzUhqUNWdMTJ5" role="row" aria-rowindex="12"
																	aria-selected="false" aria-setsize="14" draggable="true"
																	style="--ylx-folder-depth: 0;">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:playlist:7r8QOLtzDjZfAOeQObDsYz"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:playlist:7r8QOLtzDjZfAOeQObDsYz listrow-subtitle-spotify:playlist:7r8QOLtzDjZfAOeQObDsYz"
																				aria-describedby="onClickHintspotify:playlist:7r8QOLtzDjZfAOeQObDsYz"
																				tabindex="-1" class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:playlist:7r8QOLtzDjZfAOeQObDsYz"
																				style="display: none;"></div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px;"><img aria-hidden="true"
																								draggable="false" loading="eager"
																								src="https://image-cdn-fa.spotifycdn.com/image/ab67706c0000d72c035792750368e745e0a05f7b"
																								data-testid="entity-image" alt="Lit Songs"
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:playlist:7r8QOLtzDjZfAOeQObDsYz" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">Lit Songs</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:playlist:7r8QOLtzDjZfAOeQObDsYz" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Playlist • matt_lamb</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div class="NxEINIJHGytq4gF1r2N1  vSC5QuwmzUhqUNWdMTJ5" role="row" aria-rowindex="13"
																	aria-selected="false" aria-setsize="14" draggable="true"
																	style="--ylx-folder-depth: 0;">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:playlist:5UhZzcsZbeLxENDB4lx5ij"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:playlist:5UhZzcsZbeLxENDB4lx5ij listrow-subtitle-spotify:playlist:5UhZzcsZbeLxENDB4lx5ij"
																				aria-describedby="onClickHintspotify:playlist:5UhZzcsZbeLxENDB4lx5ij"
																				tabindex="-1" class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:playlist:5UhZzcsZbeLxENDB4lx5ij"
																				style="display: none;"></div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #B80000;">
																							<div aria-label="no" class="Ozitxbqs1vcOukDz3GDw"><svg
																									data-encore-id="icon" role="img" aria-hidden="true"
																									class="e-9911-icon e-9911-baseline" data-testid="playlist"
																									viewBox="0 0 24 24">
																									<path
																										d="M6 3h15v15.167a3.5 3.5 0 1 1-3.5-3.5H19V5H8v13.167a3.5 3.5 0 1 1-3.5-3.5H6V3zm0 13.667H4.5a1.5 1.5 0 1 0 1.5 1.5v-1.5zm13 0h-1.5a1.5 1.5 0 1 0 1.5 1.5v-1.5z">
																									</path>
																								</svg></div>
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:playlist:5UhZzcsZbeLxENDB4lx5ij" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">no</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:playlist:5UhZzcsZbeLxENDB4lx5ij" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span
																						class="NVHSG1CguVgjg5bJ64_Z">Playlist • hagan</span></p>
																			</div>
																		</span>
																	</div>
																</div>
																<div class="NxEINIJHGytq4gF1r2N1 XNjgtSbyhshr7YQcVvry vSC5QuwmzUhqUNWdMTJ5" role="row"
																	aria-rowindex="14" aria-selected="false" aria-setsize="14" draggable="true">
																	<div role="gridcell" aria-colindex="1">
																		<div
																			class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0 Box-sc-8t9c76-0 dUGCIT fYWNdY4zhj4OX_T2Xtg6 ZZsPF3Sn4h7m0_5Clhk0"
																			data-encore-id="listRow" role="group"
																			aria-labelledby="listrow-title-spotify:collection:your-episodes"
																			style="--box-padding: 8px; --box-min-block-size: 56px; --box-hover-animation-duration: 0ms;">
																			<div role="button" aria-disabled="false"
																				aria-labelledby="listrow-title-spotify:collection:your-episodes listrow-subtitle-spotify:collection:your-episodes"
																				aria-describedby="onClickHintspotify:collection:your-episodes" tabindex="-1"
																				class="RowButton-sc-xxkq4e-0 cRPTAY"></div>
																			<div id="onClickHintspotify:collection:your-episodes" style="display: none;">
																			</div>
																			<div class="Areas__HeaderSideArea-sc-8gfrea-1 ljvfQS">
																				<div class="Areas__HeaderSideAreaFlexContainer-sc-8gfrea-2 hvZiQp">
																					<div class="">
																						<div class="vreceNX3ABcxyddeS83B GSgVaqJa8VEp5mKoIN0b g3kBhX1E4EYEC2NFhhxG"
																							style="width: 48px; height: 48px; --extracted-entity-color: #006050;"><img
																								aria-hidden="true" draggable="false" loading="eager"
																								src="https://misc.spotifycdn.com/your-episodes/SE-300.png"
																								data-testid="entity-image" alt="Your Episodes"
																								class="mMx2LUixlnN_Fu45JpFB iJp40IxKg6emF6KYJ414 yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																						</div>
																					</div>
																				</div>
																			</div>
																			<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																				<div
																					class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																				</div>
																			</div>
																		</div><span class="c1PJ2LHU0EnzyA0jDc1j">
																			<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP oaKRK4WllExdXORQIlFZ UZYGjsTEkEen6hFQe194"
																				data-encore-id="listRowTitle"
																				id="listrow-title-spotify:collection:your-episodes" dir="auto"><span
																					class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">Your Episodes</span></p>
																			<div class="iKNK2nAjtbavMKjPPJtJ">
																				<p class="e-9911-text encore-text-body-small encore-internal-color-text-subdued ListRowDetails__ListRowDetailText-sc-sozu4l-0 hxCObm oaKRK4WllExdXORQIlFZ"
																					data-encore-id="listRowSubtitle"
																					id="listrow-subtitle-spotify:collection:your-episodes" dir="auto"><span
																						class="Gxl7UDkumVYX3WtQEnb8"></span><span class="NVHSG1CguVgjg5bJ64_Z">Saved
																						&amp; downloaded episodes</span></p>
																			</div>
																		</span>
																	</div>
																</div>
															</div>
															<div data-testid="bottom-sentinel" class="qnYVzttodnzg9WdrVQ1p" role="presentation"
																style="height: calc(100% - 384px);">
																<div role="presentation" style="height: 512px;"></div>
																<div class="eC25_w41L83mXDCqdm_A" role="row" aria-rowindex="1"
																	style="height: calc(100% - 512px);"></div>
															</div>
														</div>
													</div>
												</div>
											</div>
										</div>
									</div>
									<div
										class="os-scrollbar os-scrollbar-horizontal os-theme-spotify os-scrollbar-auto-hide os-scrollbar-auto-hide-hidden os-scrollbar-handle-interactive os-scrollbar-track-interactive os-scrollbar-cornerless os-scrollbar-unusable"
										style="--os-viewport-percent: 1; --os-scroll-direction: 0;">
										<div class="os-scrollbar-track">
											<div class="os-scrollbar-handle"></div>
										</div>
									</div>
									<div
										class="os-scrollbar os-scrollbar-vertical os-theme-spotify os-scrollbar-auto-hide os-scrollbar-auto-hide-hidden os-scrollbar-handle-interactive os-scrollbar-track-interactive os-scrollbar-visible os-scrollbar-cornerless"
										style="--os-viewport-percent: 0.641; --os-scroll-direction: 0;">
										<div class="os-scrollbar-track">
											<div class="os-scrollbar-handle"></div>
										</div>
									</div>
								</div>
							</div>
							<div class="YNnobzGm5w3XKBniKdW9" data-testid="left-sidebar-footer"></div>
						</div>
					</nav>
					<div data-testid="LayoutResizer__resize-bar" class="LayoutResizer__resize-bar LayoutResizer__inline-end">
						<label class="hidden-visually">Resize main navigation<input class="LayoutResizer__input" type="range"
								min="72" max="360" step="10" value="72"></label></div>
				</div>
				<div class="JG5J9NWJkaUO9fiKECMA">
					<footer class="yglmI5m3fCc8baD1Kwdw K7b2iysmIbvKo8RqRbc5" data-testid="now-playing-bar"
						data-testadtype="ad-type-none">
						<div class="udArIAqnfUQPQew2VAns">
							<div class="snFK6_ei0caqvFI6As9Q">
								<div data-testid="now-playing-widget" class="deomraqfhIAoSB3SgXpu" role="contentinfo"
									aria-label="Now playing: Cool by Daniel Caesar">
									<div data-testid="CoverSlotCollapsed__container" class="GQ5_gIWzIqAfBdmQm8yJ IcyWfMS5VkeOhaI7OWIx">
										<div draggable="true"><button type="button" data-testid="cover-art-button"
												class="HD9s7U5E1RLSWKpXmrqx" aria-label="Now playing view">
												<div class="BFR9Zt3zpL8BATBMiwQB">
													<div class="H0HbpIM3UrcupWIAjLWu" aria-hidden="true" style="width: 56px; height: 56px;">
														<div class="zmOtW0vqqn1qpZrtQ_w9"><svg data-encore-id="icon" role="img" aria-hidden="true"
																class="e-9911-icon e-9911-baseline" data-testid="track" viewBox="0 0 24 24">
																<path
																	d="M6 3h15v15.167a3.5 3.5 0 1 1-3.5-3.5H19V5H8v13.167a3.5 3.5 0 1 1-3.5-3.5H6V3zm0 13.667H4.5a1.5 1.5 0 1 0 1.5 1.5v-1.5zm13 0h-1.5a1.5 1.5 0 1 0 1.5 1.5v-1.5z">
																</path>
															</svg></div><img aria-hidden="false" draggable="false" loading="eager"
															src="https://i.scdn.co/image/ab67616d000048517c68face1dc58127f3a7b1cc"
															data-testid="cover-art-image" alt=""
															class="mMx2LUixlnN_Fu45JpFB FqmFsMhuF4D0s35Z62Js Yn2Ei5QZn19gria6LjZj">
													</div>
												</div>
											</button></div><button class="_9sCL61nGvQFXv2u02jXw" aria-label="Collapse"
											aria-pressed="true"><svg data-encore-id="icon" role="img" aria-hidden="true"
												class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
												style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
												<path
													d="M.47 4.97a.75.75 0 0 1 1.06 0L8 11.44l6.47-6.47a.75.75 0 1 1 1.06 1.06L8 13.56.47 6.03a.75.75 0 0 1 0-1.06z">
												</path>
											</svg></button>
									</div>
									<div class="j96cpCtZAIdqxcDrYHPI iZrIHsls0lCEhoMDA9kc">
										<div class="PcH6VnzkkDqD36P93i9Q">
											<div class="eSMjmiD29Ox35O95waw6"><span class="cpltqpeZsQmmXy7qZgb9"><span
														class="PGSe59fD1Hwc9yUM2d3U" style="--marquee-width: 80px;">
														<div class="e-9911-text encore-text-body-small K9Nj3oI7bTNFh5AGp5GA" data-encore-id="text"
															data-testid="context-item-info-title" dir="auto"><span draggable="true"><a
																	draggable="false" data-testid="context-item-link"
																	href="/album/7ivbFszr1TbVadj89BIy1y">Cool</a></span></div>
													</span></span></div>
										</div>
										<div class="p2ya1fQ3o9pY4alcW0o4 MrkH0O1OzmNv_oCQdvI8"></div>
										<div class="w_TTPh4y9H1YD6UrTMHa">
											<div class="eSMjmiD29Ox35O95waw6"><span class="cpltqpeZsQmmXy7qZgb9"><span
														class="PGSe59fD1Hwc9yUM2d3U" style="--marquee-width: 80px;">
														<div
															class="e-9911-text encore-text-marginal encore-internal-color-text-subdued w_TTPh4y9H1YD6UrTMHa"
															data-encore-id="text" data-testid="context-item-info-subtitles"><span><a draggable="true"
																	data-testid="context-item-info-artist" dir="auto"
																	href="/artist/20wkVLutqVOYrc0kxFs7rA">Daniel Caesar</a></span></div>
													</span></span></div>
										</div>
									</div>
									<div class="ZbFkATBbLkWh2SHMXDt6"><button aria-checked="true"
											class="Button-sc-1dqy6lx-0 gDSiSh e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only e-9911-button-tertiary--condensed"
											aria-label="Add to playlist" data-encore-id="buttonTertiary"><span aria-hidden="true"
												class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
													class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
													style="--encore-icon-fill: var(--text-bright-accent, #107434); --encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
													<path
														d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm11.748-1.97a.75.75 0 0 0-1.06-1.06l-4.47 4.47-1.405-1.406a.75.75 0 1 0-1.061 1.06l2.466 2.467 5.53-5.53z">
													</path>
												</svg></span></button></div>
								</div>
							</div>
							<div class="sVv2OQORCQ4kf6iKfUTF">
								<div class="gItY2hnfCB4TsDJCkPiO" data-testid="player-controls" dir="ltr" aria-label="Player controls">
									<div class="XrZ1iHVHAPMya3jkB2sa" data-testid="general-controls">
										<div class="NKUrT1GciYXAEEUtagN1"><button role="switch" aria-checked="false"
												data-testid="control-button-shuffle"
												class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only"
												aria-label="Enable shuffle" data-encore-id="buttonTertiary"><span aria-hidden="true"
													class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
														class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
														style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
														<path
															d="M13.151.922a.75.75 0 1 0-1.06 1.06L13.109 3H11.16a3.75 3.75 0 0 0-2.873 1.34l-6.173 7.356A2.25 2.25 0 0 1 .39 12.5H0V14h.391a3.75 3.75 0 0 0 2.873-1.34l6.173-7.356a2.25 2.25 0 0 1 1.724-.804h1.947l-1.017 1.018a.75.75 0 0 0 1.06 1.06L15.98 3.75 13.15.922zM.391 3.5H0V2h.391c1.109 0 2.16.49 2.873 1.34L4.89 5.277l-.979 1.167-1.796-2.14A2.25 2.25 0 0 0 .39 3.5z">
														</path>
														<path
															d="m7.5 10.723.98-1.167.957 1.14a2.25 2.25 0 0 0 1.724.804h1.947l-1.017-1.018a.75.75 0 1 1 1.06-1.06l2.829 2.828-2.829 2.828a.75.75 0 1 1-1.06-1.06L13.109 13H11.16a3.75 3.75 0 0 1-2.873-1.34l-.787-.938z">
														</path>
													</svg></span></button><button data-testid="control-button-skip-back"
												class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only"
												aria-label="Previous" data-encore-id="buttonTertiary"><span aria-hidden="true"
													class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
														class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
														style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
														<path
															d="M3.3 1a.7.7 0 0 1 .7.7v5.15l9.95-5.744a.7.7 0 0 1 1.05.606v12.575a.7.7 0 0 1-1.05.607L4 9.149V14.3a.7.7 0 0 1-.7.7H1.7a.7.7 0 0 1-.7-.7V1.7a.7.7 0 0 1 .7-.7h1.6z">
														</path>
													</svg></span></button></div><button data-testid="control-button-playpause" aria-label="Play"
											data-encore-id="buttonPrimary" data-is-icon-only="true"
											class="e-9911-button-primary e-9911-button"><span
												class="e-9911-baseline e-9911-overflow-wrap-anywhere e-9911-button-primary__inner encore-inverted-light-set e-9911-button-icon-only--small"><span
													aria-hidden="true" class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img"
														aria-hidden="true" class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
														style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
														<path
															d="M3 1.713a.7.7 0 0 1 1.05-.607l10.89 6.288a.7.7 0 0 1 0 1.212L4.05 14.894A.7.7 0 0 1 3 14.288V1.713z">
														</path>
													</svg></span></span></button>
										<div class="Qt226Z4rBQs53aedRQBQ"><button data-testid="control-button-skip-forward"
												class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only"
												aria-label="Next" data-encore-id="buttonTertiary"><span aria-hidden="true"
													class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
														class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
														style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
														<path
															d="M12.7 1a.7.7 0 0 0-.7.7v5.15L2.05 1.107A.7.7 0 0 0 1 1.712v12.575a.7.7 0 0 0 1.05.607L12 9.149V14.3a.7.7 0 0 0 .7.7h1.6a.7.7 0 0 0 .7-.7V1.7a.7.7 0 0 0-.7-.7h-1.6z">
														</path>
													</svg></span></button><button data-testid="control-button-repeat" role="checkbox"
												aria-checked="mixed"
												class="Button-sc-1dqy6lx-0 bLLOzN e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only vW9NFcNIj8useE43Vx9G"
												aria-label="Disable repeat" data-encore-id="buttonTertiary"><span aria-hidden="true"
													class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
														class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
														style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
														<path
															d="M0 4.75A3.75 3.75 0 0 1 3.75 1h.75v1.5h-.75A2.25 2.25 0 0 0 1.5 4.75v5A2.25 2.25 0 0 0 3.75 12H5v1.5H3.75A3.75 3.75 0 0 1 0 9.75v-5ZM12.25 2.5a2.25 2.25 0 0 1 2.25 2.25v5A2.25 2.25 0 0 1 12.25 12H9.81l1.018-1.018a.75.75 0 0 0-1.06-1.06L6.939 12.75l2.829 2.828a.75.75 0 1 0 1.06-1.06L9.811 13.5h2.439A3.75 3.75 0 0 0 16 9.75v-5A3.75 3.75 0 0 0 12.25 1h-.75v1.5h.75Z">
														</path>
														<path
															d="m8 1.85.77.694H6.095V1.488c.697-.051 1.2-.18 1.507-.385.316-.205.51-.51.583-.913h1.32V8H8V1.85Z">
														</path>
														<path d="M8.77 2.544 8 1.85v.693h.77Z"></path>
													</svg></span></button></div>
									</div>
									<div class="pn5V0OzovI9p6b8nWq8p gglUjikTBtMzCZFgSmpS">
										<div
											class="e-9911-text encore-text-marginal encore-internal-color-text-subdued IPbBrI6yF4zhaizFmrg6"
											data-encore-id="text" data-testid="playback-position">2:16</div>
										<div class="B1vgcMXBqOxgMxXh5j1f">
											<div class="p1ULRzPc4bD8eQ4T_wyp DFtdzavKSbEhwKYkPTa6 ZqlJ1uWjMeen9ye7Y7GC"
												data-testid="playback-progressbar"><label class="hidden-visually">Change progress<input
														type="range" min="0" max="244189" step="5000" aria-valuetext="2:16/4:04"
														value="136499"></label>
												<div class="TywOcKZEqNynWecCiATc" data-testid="progress-bar"
													style="--progress-bar-duration: 1000ms; --progress-bar-transform: 55.89891436551196%; --hover-bar-transform: 0%;">
													<div class="NoOAOv6U6vtqj_ybS1Cd" data-testid="progress-bar-background">
														<div class="w699O0LgQRghXyl3bs9u">
															<div class="i_sFCqXc9E62sDov95kp"></div>
														</div>
														<div class="w699O0LgQRghXyl3bs9u">
															<div class="epWhU7hHGktzlO_dop6z oShi2lRbnhFkEr2LlUqC"></div>
														</div>
														<div class="Vis45PPawTyED7Lt2_LI oShi2lRbnhFkEr2LlUqC"></div>
													</div>
													<div style="width: 100%;"></div>
												</div>
											</div>
										</div>
										<div
											class="e-9911-text encore-text-marginal encore-internal-color-text-subdued kQqIrFPM5PjMWb5qUS56 DSdahCi0SDG37V9ZmsGO"
											data-encore-id="text" data-testid="playback-duration" data-test-position="136499">4:04</div>
									</div>
								</div>
							</div>
							<div class="pLifNBuHRY8cZkZyEqwL">
								<div class="mwpJrmCgLlVkJVtWjlI1"><button data-testid="control-button-npv" data-active="true"
										aria-pressed="true" data-restore-focus-key="now_playing_view"
										class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only KAZD28usA1vPz5GVpm63 RK45o6dbvO1mb0wQtSwq EHxL6K_6WWDlTCZP6x5w"
										aria-label="Now playing view" data-encore-id="buttonTertiary"><span aria-hidden="true"
											class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
												class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
												style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
												<path d="M11.196 8 6 5v6l5.196-3z"></path>
												<path
													d="M15.002 1.75A1.75 1.75 0 0 0 13.252 0h-10.5a1.75 1.75 0 0 0-1.75 1.75v12.5c0 .966.783 1.75 1.75 1.75h10.5a1.75 1.75 0 0 0 1.75-1.75V1.75zm-1.75-.25a.25.25 0 0 1 .25.25v12.5a.25.25 0 0 1-.25.25h-10.5a.25.25 0 0 1-.25-.25V1.75a.25.25 0 0 1 .25-.25h10.5z">
												</path>
											</svg></span></button><button data-testid="lyrics-button" data-active="false" aria-pressed="false"
										class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only KAZD28usA1vPz5GVpm63 Xmv2oAnTB85QE4sqbK00"
										aria-label="Lyrics" data-encore-id="buttonTertiary"><span aria-hidden="true"
											class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
												class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
												style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
												<path
													d="M13.426 2.574a2.831 2.831 0 0 0-4.797 1.55l3.247 3.247a2.831 2.831 0 0 0 1.55-4.797zM10.5 8.118l-2.619-2.62A63303.13 63303.13 0 0 0 4.74 9.075L2.065 12.12a1.287 1.287 0 0 0 1.816 1.816l3.06-2.688 3.56-3.129zM7.12 4.094a4.331 4.331 0 1 1 4.786 4.786l-3.974 3.493-3.06 2.689a2.787 2.787 0 0 1-3.933-3.933l2.676-3.045 3.505-3.99z">
												</path>
											</svg></span></button>
									<div class="NxEINIJHGytq4gF1r2N1 or84FBarW2zQhXfB9VFb odS2IW9wfNVHhkhc0l_X XNjgtSbyhshr7YQcVvry">
										<button data-testid="control-button-queue" data-active="false" aria-pressed="false"
											data-restore-focus-key="queue"
											class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only KAZD28usA1vPz5GVpm63"
											aria-label="Queue" data-encore-id="buttonTertiary"><span aria-hidden="true"
												class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
													class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
													style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
													<path
														d="M15 15H1v-1.5h14V15zm0-4.5H1V9h14v1.5zm-14-7A2.5 2.5 0 0 1 3.5 1h9a2.5 2.5 0 0 1 0 5h-9A2.5 2.5 0 0 1 1 3.5zm2.5-1a1 1 0 0 0 0 2h9a1 1 0 1 0 0-2h-9z">
													</path>
												</svg></span></button></div><span role="presentation"><button data-active="false"
											aria-pressed="false" data-restore-focus-key="device_picker"
											aria-describedby="connect-message-nudge"
											class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only KAZD28usA1vPz5GVpm63"
											aria-label="Connect to a device" data-encore-id="buttonTertiary"><span aria-hidden="true"
												class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
													class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
													style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
													<path
														d="M6 2.75C6 1.784 6.784 1 7.75 1h6.5c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 14.25 15h-6.5A1.75 1.75 0 0 1 6 13.25V2.75zm1.75-.25a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25V2.75a.25.25 0 0 0-.25-.25h-6.5zm-6 0a.25.25 0 0 0-.25.25v6.5c0 .138.112.25.25.25H4V11H1.75A1.75 1.75 0 0 1 0 9.25v-6.5C0 1.784.784 1 1.75 1H4v1.5H1.75zM4 15H2v-1.5h2V15z">
													</path>
													<path d="M13 10a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm-1-5a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"></path>
												</svg></span></button></span>
									<div class="G4n5bTzWUvlftzDwrFVG ExuDUBJ7bk8vT6INnm9F" data-testid="volume-bar" dir="ltr"
										style="--button-size: 32px; --slider-width: 100%;"><button
											class="rT09bwCEwXECMbLbX_7A control-button" aria-label="Mute" aria-describedby="volume-icon"
											data-testid="volume-bar-toggle-mute-button"><svg data-encore-id="icon" role="presentation"
												aria-label="Volume high" aria-hidden="false" class="e-9911-icon e-9911-baseline"
												id="volume-icon" viewBox="0 0 16 16"
												style="--encore-icon-height: var(--encore-graphic-size-informative-smaller); --encore-icon-width: var(--encore-graphic-size-informative-smaller);">
												<path
													d="M9.741.85a.75.75 0 0 1 .375.65v13a.75.75 0 0 1-1.125.65l-6.925-4a3.642 3.642 0 0 1-1.33-4.967 3.639 3.639 0 0 1 1.33-1.332l6.925-4a.75.75 0 0 1 .75 0zm-6.924 5.3a2.139 2.139 0 0 0 0 3.7l5.8 3.35V2.8l-5.8 3.35zm8.683 4.29V5.56a2.75 2.75 0 0 1 0 4.88z">
												</path>
												<path d="M11.5 13.614a5.752 5.752 0 0 0 0-11.228v1.55a4.252 4.252 0 0 1 0 8.127v1.55z"></path>
											</svg></button>
										<div class="tIr7C6B0Pt6YKdOnqaqj">
											<div class="p1ULRzPc4bD8eQ4T_wyp DFtdzavKSbEhwKYkPTa6"><label class="hidden-visually">Change
													volume<input type="range" min="0" max="1" step="0.1" value="1"></label>
												<div class="TywOcKZEqNynWecCiATc" data-testid="progress-bar"
													style="--progress-bar-transform: 100%; --hover-bar-transform: 0%;">
													<div class="NoOAOv6U6vtqj_ybS1Cd" data-testid="progress-bar-background">
														<div class="w699O0LgQRghXyl3bs9u">
															<div class="i_sFCqXc9E62sDov95kp"></div>
														</div>
														<div class="w699O0LgQRghXyl3bs9u">
															<div class="epWhU7hHGktzlO_dop6z"></div>
														</div>
														<div class="Vis45PPawTyED7Lt2_LI"></div>
													</div>
													<div style="width: 100%;"></div>
												</div>
											</div>
										</div>
									</div><button data-testid="pip-toggle-button" data-active="false" aria-pressed="false"
										class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only KAZD28usA1vPz5GVpm63"
										aria-label="Open Miniplayer" data-encore-id="buttonTertiary"><span aria-hidden="true"
											class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
												class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
												style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
												<path
													d="M16 2.45c0-.8-.65-1.45-1.45-1.45H1.45C.65 1 0 1.65 0 2.45v11.1C0 14.35.65 15 1.45 15h5.557v-1.5H1.5v-11h13V7H16V2.45z">
												</path>
												<path
													d="M15.25 9.007a.75.75 0 0 1 .75.75v4.493a.75.75 0 0 1-.75.75H9.325a.75.75 0 0 1-.75-.75V9.757a.75.75 0 0 1 .75-.75h5.925z">
												</path>
											</svg></span></button><button data-testid="fullscreen-mode-button" data-active="false"
										aria-pressed="false"
										class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only KAZD28usA1vPz5GVpm63 control-button"
										aria-label="Enter full screen" data-encore-id="buttonTertiary"><span aria-hidden="true"
											class="e-9911-button__icon-wrapper"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"
												xmlns="http://www.w3.org/2000/svg">
												<path fill-rule="evenodd" clip-rule="evenodd"
													d="M0.25 3C0.25 2.0335 1.0335 1.25 2 1.25H5.375V2.75H2C1.86193 2.75 1.75 2.86193 1.75 3V5.42857H0.25V3ZM14 2.75H10.625V1.25H14C14.9665 1.25 15.75 2.0335 15.75 3V5.42857H14.25V3C14.25 2.86193 14.1381 2.75 14 2.75ZM1.75 10.5714V13C1.75 13.1381 1.86193 13.25 2 13.25H5.375V14.75H2C1.0335 14.75 0.25 13.9665 0.25 13V10.5714H1.75ZM14.25 13V10.5714H15.75V13C15.75 13.9665 14.9665 14.75 14 14.75H10.625V13.25H14C14.1381 13.25 14.25 13.1381 14.25 13Z"
													fill="currentColor"></path>
											</svg></span></button>
								</div>
							</div>
						</div>
					</footer>
				</div>
				<div class="jEMA2gVoLgPQqAFrPhFw">
					<div class="main-view-container">
						<div class="under-main-view"></div>
						<div data-overlayscrollbars-initialize="true" class="main-view-container__scroll-node ZjfaJlGQZ42nCWjD3FDm"
							data-overlayscrollbars="host">
							<div class="" data-overlayscrollbars-viewport="scrollbarHidden overflowXHidden overflowYScroll"
								tabindex="-1"
								style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; top: 0px; right: auto; left: 0px; width: calc(100% + 0px); padding: 0px;">
								<div class="main-view-container__scroll-node-child" style="min-height: calc(-673px + 100vh);">
									<main class="T0fKO6B7LQSCE_VaSM1P" tabindex="-1" aria-label="nzgative">
										<section class="cubl27eU3uN3hmAiqdmQ">
											<div class="contentSpacing">
												<section class="QyANtc_r7ff_tqrf5Bvc Shelf MKCgGhu_c8l6hsVuee46 yGNmd_gHDqy6we9VwoNj"
													data-shelf="shelf" data-testid="component-shelf" aria-label="Following"
													style="--shelf-min-height: 260px;">
													<div class="q8AZzDc_1BumBHZg0tZb">
														<div
															class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 efnFkI _WZEvLWCKIvdsvaCs6x5 Box-sc-8t9c76-0 efnFkI _WZEvLWCKIvdsvaCs6x5"
															data-encore-id="listRow" role="group" aria-labelledby="listrow-title-:r7:"
															data-testid="rich-title-row-shelf-header"
															style="--box-padding-block-start: 8px; --box-padding-block-end: 8px; --box-padding-inline-start: none; --box-padding-inline-end: none; --box-min-block-size: 56px;">
															<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
																<div class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																	<h1
																		class="e-9911-text encore-text-title-medium encore-internal-color-text-base ListRowTitle__ListRowText-sc-1xe2if1-1 eFGzcP KpzkVLd9fh2ZrKqZoFg5"
																		data-encore-id="listRowTitle" id=":r7:" aria-describedby=":r6:"><span
																			class="ListRowTitle__LineClamp-sc-1xe2if1-0 jjpOuK">Following</span></h1>
																</div>
															</div>
														</div>
													</div>
													<div class="hWGxHSAKACFWXowXPDTP">
														<div class="WqHooc2Y_6VuGI84LxQj"><button
																class="LegacyChip__LegacyChipComponent-sc-tzfq94-0 fZfoaE encore-text-body-small"
																role="checkbox" aria-checked="true" data-encore-id="chip"><span
																	class="LegacyChipInner__ChipInnerComponent-sc-1qguixk-0 bVqsHn encore-inverted-light-set">All</span></button><button
																class="LegacyChip__LegacyChipComponent-sc-tzfq94-0 fJQBhR encore-text-body-small"
																role="checkbox" aria-checked="false" data-encore-id="chip"><span
																	class="LegacyChipInner__ChipInnerComponent-sc-1qguixk-0 jVBuxI">Artists</span></button><button
																class="LegacyChip__LegacyChipComponent-sc-tzfq94-0 fJQBhR encore-text-body-small"
																role="checkbox" aria-checked="false" data-encore-id="chip"><span
																	class="LegacyChipInner__ChipInnerComponent-sc-1qguixk-0 jVBuxI">Friends</span></button>
														</div>
													</div>
													<div role="presentation" data-testid="grid-container"
														class="iKwGKEfAfW7Rkx2_Ba4E Z4InHgCs2uhk0MU93y_a PUv6m4kpDj81VpqgWuLG"
														style="--min-column-width: 180px;">
														<div
															class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-Box-sc-1njtxi4-0 faRaKi aAYpzGljXQv1_zfopxaH Card Box-sc-1njtxi4-0 faRaKi aAYpzGljXQv1_zfopxaH Card"
															data-encore-id="card" aria-labelledby="card-title-spotify:artist:7dGJo4pcD2V6oG8kP0tJRR-0"
															draggable="true"
															style="--box-padding-block-start: 12px; --box-padding-block-end: 12px; --box-padding-inline-start: 12px; --box-padding-inline-end: 12px;">
															<div role="button" aria-disabled="false"
																aria-labelledby="card-title-spotify:artist:7dGJo4pcD2V6oG8kP0tJRR-0 card-subtitle-spotify:artist:7dGJo4pcD2V6oG8kP0tJRR-0"
																aria-describedby="onClickHintspotify:artist:7dGJo4pcD2V6oG8kP0tJRR-0" tabindex="0"
																class="CardButton-sc-g9vf2u-0 eWZOJQ"></div>
															<div id="onClickHintspotify:artist:7dGJo4pcD2V6oG8kP0tJRR-0" style="display: none;"></div>
															<div class="xBV4XgMq0gC5lQICFWY_">
																<div class="GOcsybnoHYyJGQGDRuwj MxmW8QkHqHWtuhO589PV">
																	<div><img aria-hidden="false" draggable="false" loading="lazy"
																			src="https://i.scdn.co/image/ab67616100005174a00b11c129b27a88fc72f36b"
																			data-testid="card-image" alt=""
																			class="mMx2LUixlnN_Fu45JpFB yMQTWVwLJ5bV8VGiaqU3 MxmW8QkHqHWtuhO589PV yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																	</div>
																</div>
																<div class="woJQ5t2YiaJhjTv_KE7p">
																	<div class="ix_8kg3iUb9VS5SmTnBY"><button data-testid="play-button"
																			aria-label="Play Eminem" data-encore-id="buttonPrimary" data-is-icon-only="true"
																			class="e-9911-button-primary e-9911-button"><span
																				class="e-9911-baseline e-9911-overflow-wrap-anywhere e-9911-button-primary__inner encore-bright-accent-set e-9911-button-icon-only--medium"><span
																					aria-hidden="true" class="e-9911-button__icon-wrapper"><svg
																						data-encore-id="icon" role="img" aria-hidden="true"
																						class="e-9911-icon e-9911-baseline" viewBox="0 0 24 24">
																						<path
																							d="m7.05 3.606 13.49 7.788a.7.7 0 0 1 0 1.212L7.05 20.394A.7.7 0 0 1 6 19.788V4.212a.7.7 0 0 1 1.05-.606z">
																						</path>
																					</svg></span></span></button></div>
																</div>
															</div>
															<div
																class="Areas__InteractiveArea-sc-1tea2mc-0 Areas__MainArea-sc-1tea2mc-1 MWEhk kLALqL">
																<div class="Areas__InteractiveArea-sc-1tea2mc-0 Areas__Column-sc-1tea2mc-2 MWEhk yMCdi">
																	<a draggable="false" class="Gi6Lr1whYBA2jutvHvjQ" tabindex="-1"
																		href="/artist/7dGJo4pcD2V6oG8kP0tJRR">
																		<p class="e-9911-text encore-text-body-medium CardTitle__CardText-sc-1h38un4-1 eznGBk xHz124sSHSCYHecLCTfi"
																			data-encore-id="cardTitle" id="card-title-spotify:artist:7dGJo4pcD2V6oG8kP0tJRR-0"
																			aria-describedby="onClickHintspotify:artist:7dGJo4pcD2V6oG8kP0tJRR-0"
																			title="Eminem" dir="auto"><span
																				class="CardTitle__LineClamp-sc-1h38un4-0 RBShQ"><span
																					class="">Eminem</span></span></p>
																	</a>
																	<div
																		class="e-9911-text encore-text-body-small encore-internal-color-text-subdued CardDetails__CardDetailText-sc-1gdonml-1 kNtRLK"
																		data-encore-id="cardSubtitle"
																		id="card-subtitle-spotify:artist:7dGJo4pcD2V6oG8kP0tJRR-0" dir="auto"><span
																			class="CardDetails__LineClamp-sc-1gdonml-0 sVzSB">
																			<div
																				class="e-9911-text encore-text-body-small encore-internal-color-text-subdued i6jA7UnVNDJFGlAgtutp JS9WYvoqyy3vUXqMt5Hv"
																				data-encore-id="text"><span>Artist</span></div>
																		</span></div>
																</div>
															</div>
														</div>
														<div
															class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-Box-sc-1njtxi4-0 faRaKi aAYpzGljXQv1_zfopxaH Card Box-sc-1njtxi4-0 faRaKi aAYpzGljXQv1_zfopxaH Card"
															data-encore-id="card" aria-labelledby="card-title-spotify:artist:5K4W6rqBFWDnAN6FQUkS6x-1"
															draggable="true"
															style="--box-padding-block-start: 12px; --box-padding-block-end: 12px; --box-padding-inline-start: 12px; --box-padding-inline-end: 12px;">
															<div role="button" aria-disabled="false"
																aria-labelledby="card-title-spotify:artist:5K4W6rqBFWDnAN6FQUkS6x-1 card-subtitle-spotify:artist:5K4W6rqBFWDnAN6FQUkS6x-1"
																aria-describedby="onClickHintspotify:artist:5K4W6rqBFWDnAN6FQUkS6x-1" tabindex="0"
																class="CardButton-sc-g9vf2u-0 eWZOJQ"></div>
															<div id="onClickHintspotify:artist:5K4W6rqBFWDnAN6FQUkS6x-1" style="display: none;"></div>
															<div class="xBV4XgMq0gC5lQICFWY_">
																<div class="GOcsybnoHYyJGQGDRuwj MxmW8QkHqHWtuhO589PV">
																	<div><img aria-hidden="false" draggable="false" loading="lazy"
																			src="https://i.scdn.co/image/ab676161000051746e835a500e791bf9c27a422a"
																			data-testid="card-image" alt=""
																			class="mMx2LUixlnN_Fu45JpFB yMQTWVwLJ5bV8VGiaqU3 MxmW8QkHqHWtuhO589PV yOKoknIYYzAE90pe7_SE Yn2Ei5QZn19gria6LjZj">
																	</div>
																</div>
																<div class="woJQ5t2YiaJhjTv_KE7p">
																	<div class="ix_8kg3iUb9VS5SmTnBY"><button data-testid="play-button"
																			aria-label="Play Kanye West" data-encore-id="buttonPrimary"
																			data-is-icon-only="true" class="e-9911-button-primary e-9911-button"><span
																				class="e-9911-baseline e-9911-overflow-wrap-anywhere e-9911-button-primary__inner encore-bright-accent-set e-9911-button-icon-only--medium"><span
																					aria-hidden="true" class="e-9911-button__icon-wrapper"><svg
																						data-encore-id="icon" role="img" aria-hidden="true"
																						class="e-9911-icon e-9911-baseline" viewBox="0 0 24 24">
																						<path
																							d="m7.05 3.606 13.49 7.788a.7.7 0 0 1 0 1.212L7.05 20.394A.7.7 0 0 1 6 19.788V4.212a.7.7 0 0 1 1.05-.606z">
																						</path>
																					</svg></span></span></button></div>
																</div>
															</div>
															<div
																class="Areas__InteractiveArea-sc-1tea2mc-0 Areas__MainArea-sc-1tea2mc-1 MWEhk kLALqL">
																<div class="Areas__InteractiveArea-sc-1tea2mc-0 Areas__Column-sc-1tea2mc-2 MWEhk yMCdi">
																	<a draggable="false" class="Gi6Lr1whYBA2jutvHvjQ" tabindex="-1"
																		href="/artist/5K4W6rqBFWDnAN6FQUkS6x">
																		<p class="e-9911-text encore-text-body-medium CardTitle__CardText-sc-1h38un4-1 eznGBk xHz124sSHSCYHecLCTfi"
																			data-encore-id="cardTitle" id="card-title-spotify:artist:5K4W6rqBFWDnAN6FQUkS6x-1"
																			aria-describedby="onClickHintspotify:artist:5K4W6rqBFWDnAN6FQUkS6x-1"
																			title="Kanye West" dir="auto"><span
																				class="CardTitle__LineClamp-sc-1h38un4-0 RBShQ"><span class="">Kanye
																					West</span></span></p>
																	</a>
																	<div
																		class="e-9911-text encore-text-body-small encore-internal-color-text-subdued CardDetails__CardDetailText-sc-1gdonml-1 kNtRLK"
																		data-encore-id="cardSubtitle"
																		id="card-subtitle-spotify:artist:5K4W6rqBFWDnAN6FQUkS6x-1" dir="auto"><span
																			class="CardDetails__LineClamp-sc-1gdonml-0 sVzSB">
																			<div
																				class="e-9911-text encore-text-body-small encore-internal-color-text-subdued i6jA7UnVNDJFGlAgtutp JS9WYvoqyy3vUXqMt5Hv"
																				data-encore-id="text"><span>Artist</span></div>
																		</span></div>
																</div>
															</div>
														</div>
														<div
															class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-Box-sc-1njtxi4-0 faRaKi aAYpzGljXQv1_zfopxaH Card Box-sc-1njtxi4-0 faRaKi aAYpzGljXQv1_zfopxaH Card"
															data-encore-id="card"
															aria-labelledby="card-title-spotify:user:xfc0xcgzah4dwht454x3gda3l-2" draggable="true"
															style="--box-padding-block-start: 12px; --box-padding-block-end: 12px; --box-padding-inline-start: 12px; --box-padding-inline-end: 12px;">
															<div role="button" aria-disabled="false"
																aria-labelledby="card-title-spotify:user:xfc0xcgzah4dwht454x3gda3l-2 card-subtitle-spotify:user:xfc0xcgzah4dwht454x3gda3l-2"
																aria-describedby="onClickHintspotify:user:xfc0xcgzah4dwht454x3gda3l-2" tabindex="0"
																class="CardButton-sc-g9vf2u-0 eWZOJQ"></div>
															<div id="onClickHintspotify:user:xfc0xcgzah4dwht454x3gda3l-2" style="display: none;">
															</div>
															<div class="xBV4XgMq0gC5lQICFWY_">
																<div class="GOcsybnoHYyJGQGDRuwj MxmW8QkHqHWtuhO589PV">
																	<div><img aria-hidden="false" draggable="false" loading="lazy"
																			src="https://i.scdn.co/image/ab6775700000ee8521871b00b558b5ae57127268"
																			data-testid="card-image" alt=""
																			class="mMx2LUixlnN_Fu45JpFB yMQTWVwLJ5bV8VGiaqU3 MxmW8QkHqHWtuhO589PV Yn2Ei5QZn19gria6LjZj">
																	</div>
																</div>
															</div>
															<div
																class="Areas__InteractiveArea-sc-1tea2mc-0 Areas__MainArea-sc-1tea2mc-1 MWEhk kLALqL">
																<div class="Areas__InteractiveArea-sc-1tea2mc-0 Areas__Column-sc-1tea2mc-2 MWEhk yMCdi">
																	<a draggable="false" class="Gi6Lr1whYBA2jutvHvjQ" tabindex="-1"
																		href="/user/xfc0xcgzah4dwht454x3gda3l">
																		<p class="e-9911-text encore-text-body-medium CardTitle__CardText-sc-1h38un4-1 eznGBk xHz124sSHSCYHecLCTfi"
																			data-encore-id="cardTitle"
																			id="card-title-spotify:user:xfc0xcgzah4dwht454x3gda3l-2"
																			aria-describedby="onClickHintspotify:user:xfc0xcgzah4dwht454x3gda3l-2"
																			title="Gloamed" dir="auto"><span
																				class="CardTitle__LineClamp-sc-1h38un4-0 RBShQ"><span
																					class="">Gloamed</span></span></p>
																	</a>
																	<div
																		class="e-9911-text encore-text-body-small encore-internal-color-text-subdued CardDetails__CardDetailText-sc-1gdonml-1 kNtRLK"
																		data-encore-id="cardSubtitle"
																		id="card-subtitle-spotify:user:xfc0xcgzah4dwht454x3gda3l-2" dir="auto"><span
																			class="CardDetails__LineClamp-sc-1gdonml-0 sVzSB">
																			<div
																				class="e-9911-text encore-text-body-small encore-internal-color-text-subdued i6jA7UnVNDJFGlAgtutp JS9WYvoqyy3vUXqMt5Hv"
																				data-encore-id="text">Profile</div>
																		</span></div>
																</div>
															</div>
														</div>
														<div
															class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-Box-sc-1njtxi4-0 faRaKi aAYpzGljXQv1_zfopxaH Card Box-sc-1njtxi4-0 faRaKi aAYpzGljXQv1_zfopxaH Card"
															data-encore-id="card"
															aria-labelledby="card-title-spotify:user:e4gve9exgtrwi04igrbkp437d-3" draggable="true"
															style="--box-padding-block-start: 12px; --box-padding-block-end: 12px; --box-padding-inline-start: 12px; --box-padding-inline-end: 12px;">
															<div role="button" aria-disabled="false"
																aria-labelledby="card-title-spotify:user:e4gve9exgtrwi04igrbkp437d-3 card-subtitle-spotify:user:e4gve9exgtrwi04igrbkp437d-3"
																aria-describedby="onClickHintspotify:user:e4gve9exgtrwi04igrbkp437d-3" tabindex="0"
																class="CardButton-sc-g9vf2u-0 eWZOJQ"></div>
															<div id="onClickHintspotify:user:e4gve9exgtrwi04igrbkp437d-3" style="display: none;">
															</div>
															<div class="xBV4XgMq0gC5lQICFWY_">
																<div class="GOcsybnoHYyJGQGDRuwj MxmW8QkHqHWtuhO589PV">
																	<div><img aria-hidden="false" draggable="false" loading="lazy"
																			src="https://i.scdn.co/image/ab6775700000ee8553c5b4a011f3457a409ee5d2"
																			data-testid="card-image" alt=""
																			class="mMx2LUixlnN_Fu45JpFB yMQTWVwLJ5bV8VGiaqU3 MxmW8QkHqHWtuhO589PV Yn2Ei5QZn19gria6LjZj">
																	</div>
																</div>
															</div>
															<div
																class="Areas__InteractiveArea-sc-1tea2mc-0 Areas__MainArea-sc-1tea2mc-1 MWEhk kLALqL">
																<div class="Areas__InteractiveArea-sc-1tea2mc-0 Areas__Column-sc-1tea2mc-2 MWEhk yMCdi">
																	<a draggable="false" class="Gi6Lr1whYBA2jutvHvjQ" tabindex="-1"
																		href="/user/e4gve9exgtrwi04igrbkp437d">
																		<p class="e-9911-text encore-text-body-medium CardTitle__CardText-sc-1h38un4-1 eznGBk xHz124sSHSCYHecLCTfi"
																			data-encore-id="cardTitle"
																			id="card-title-spotify:user:e4gve9exgtrwi04igrbkp437d-3"
																			aria-describedby="onClickHintspotify:user:e4gve9exgtrwi04igrbkp437d-3" title="Kaz"
																			dir="auto"><span class="CardTitle__LineClamp-sc-1h38un4-0 RBShQ"><span
																					class="">Kaz</span></span></p>
																	</a>
																	<div
																		class="e-9911-text encore-text-body-small encore-internal-color-text-subdued CardDetails__CardDetailText-sc-1gdonml-1 kNtRLK"
																		data-encore-id="cardSubtitle"
																		id="card-subtitle-spotify:user:e4gve9exgtrwi04igrbkp437d-3" dir="auto"><span
																			class="CardDetails__LineClamp-sc-1gdonml-0 sVzSB">
																			<div
																				class="e-9911-text encore-text-body-small encore-internal-color-text-subdued i6jA7UnVNDJFGlAgtutp JS9WYvoqyy3vUXqMt5Hv"
																				data-encore-id="text">Profile</div>
																		</span></div>
																</div>
															</div>
														</div>
														<div
															class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--interactive e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-Box-sc-1njtxi4-0 faRaKi aAYpzGljXQv1_zfopxaH Card Box-sc-1njtxi4-0 faRaKi aAYpzGljXQv1_zfopxaH Card"
															data-encore-id="card"
															aria-labelledby="card-title-spotify:user:4q3bk07aqi7e5uj32w78izgbu-4" draggable="true"
															style="--box-padding-block-start: 12px; --box-padding-block-end: 12px; --box-padding-inline-start: 12px; --box-padding-inline-end: 12px;">
															<div role="button" aria-disabled="false"
																aria-labelledby="card-title-spotify:user:4q3bk07aqi7e5uj32w78izgbu-4 card-subtitle-spotify:user:4q3bk07aqi7e5uj32w78izgbu-4"
																aria-describedby="onClickHintspotify:user:4q3bk07aqi7e5uj32w78izgbu-4" tabindex="0"
																class="CardButton-sc-g9vf2u-0 eWZOJQ"></div>
															<div id="onClickHintspotify:user:4q3bk07aqi7e5uj32w78izgbu-4" style="display: none;">
															</div>
															<div class="xBV4XgMq0gC5lQICFWY_">
																<div class="GOcsybnoHYyJGQGDRuwj MxmW8QkHqHWtuhO589PV">
																	<div><img aria-hidden="false" draggable="false" loading="lazy"
																			src="https://i.scdn.co/image/ab6775700000ee85469db21111d28e61b5e6e262"
																			data-testid="card-image" alt=""
																			class="mMx2LUixlnN_Fu45JpFB yMQTWVwLJ5bV8VGiaqU3 MxmW8QkHqHWtuhO589PV Yn2Ei5QZn19gria6LjZj">
																	</div>
																</div>
															</div>
															<div
																class="Areas__InteractiveArea-sc-1tea2mc-0 Areas__MainArea-sc-1tea2mc-1 MWEhk kLALqL">
																<div class="Areas__InteractiveArea-sc-1tea2mc-0 Areas__Column-sc-1tea2mc-2 MWEhk yMCdi">
																	<a draggable="false" class="Gi6Lr1whYBA2jutvHvjQ" tabindex="-1"
																		href="/user/4q3bk07aqi7e5uj32w78izgbu">
																		<p class="e-9911-text encore-text-body-medium CardTitle__CardText-sc-1h38un4-1 eznGBk xHz124sSHSCYHecLCTfi"
																			data-encore-id="cardTitle"
																			id="card-title-spotify:user:4q3bk07aqi7e5uj32w78izgbu-4"
																			aria-describedby="onClickHintspotify:user:4q3bk07aqi7e5uj32w78izgbu-4"
																			title="Trap Flow" dir="auto"><span
																				class="CardTitle__LineClamp-sc-1h38un4-0 RBShQ"><span class="">Trap
																					Flow</span></span></p>
																	</a>
																	<div
																		class="e-9911-text encore-text-body-small encore-internal-color-text-subdued CardDetails__CardDetailText-sc-1gdonml-1 kNtRLK"
																		data-encore-id="cardSubtitle"
																		id="card-subtitle-spotify:user:4q3bk07aqi7e5uj32w78izgbu-4" dir="auto"><span
																			class="CardDetails__LineClamp-sc-1gdonml-0 sVzSB">
																			<div
																				class="e-9911-text encore-text-body-small encore-internal-color-text-subdued i6jA7UnVNDJFGlAgtutp JS9WYvoqyy3vUXqMt5Hv"
																				data-encore-id="text">Profile</div>
																		</span></div>
																</div>
															</div>
														</div>
													</div>
												</section>
											</div>
										</section>
										<div class="main-view-container__mh-footer-container">
											<hr
												class="HorizontalRule__HorizontalRuleElement-sc-198gjx4-0 gPhSUm main-view-container__mh-footer-container__separator"
												data-encore-id="horizontalRule">
											<div>
												<nav data-testid="footer-div" class="sc-jxOSlx esBjsh">
													<div class="sc-lcIPJg jJzFav">
														<div class="sc-kdBSHD ifWcoO">
															<div class="sc-fHjqPf fzcUDM">
																<ul role="list" class="TypeList__TypeListElement-sc-1jhixr6-0 nboVZ sc-hzhJZQ ibchEK"
																	data-encore-id="typeList">
																	<p data-encore-id="type" class="Type__TypeElement-sc-goli3j-0 kMPYEq">Company</p><a
																		href="https://www.spotify.com/ca-en/about-us/contact/" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu" data-ga-action="about"><span
																			data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">About</span></a><a
																		href="https://www.lifeatspotify.com/" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu" data-ga-action="jobs"><span
																			data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Jobs</span></a><a
																		href="https://newsroom.spotify.com/" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu" data-ga-action="press"><span
																			data-encore-id="type" class="Type__TypeElement-sc-goli3j-0 gxaBVX">For the
																			Record</span></a>
																</ul>
															</div>
															<div class="sc-fHjqPf fzcUDM">
																<ul role="list" class="TypeList__TypeListElement-sc-1jhixr6-0 nboVZ sc-hzhJZQ ibchEK"
																	data-encore-id="typeList">
																	<p data-encore-id="type" class="Type__TypeElement-sc-goli3j-0 kMPYEq">Communities</p>
																	<a href="https://artists.spotify.com/" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu" data-ga-action="artists"><span
																			data-encore-id="type" class="Type__TypeElement-sc-goli3j-0 gxaBVX">For
																			Artists</span></a><a href="https://developer.spotify.com/" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu" data-ga-action="developers"><span
																			data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Developers</span></a><a
																		href="https://ads.spotify.com/" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu" data-ga-action="advertising"><span
																			data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Advertising</span></a><a
																		href="https://investors.spotify.com/" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu" data-ga-action="investors"><span
																			data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Investors</span></a><a
																		href="https://spotifyforvendors.com/" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu" data-ga-action="vendors"><span
																			data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Vendors</span></a>
																</ul>
															</div>
															<div class="sc-fHjqPf fzcUDM">
																<ul role="list" class="TypeList__TypeListElement-sc-1jhixr6-0 nboVZ sc-hzhJZQ ibchEK"
																	data-encore-id="typeList">
																	<p data-encore-id="type" class="Type__TypeElement-sc-goli3j-0 kMPYEq">Useful links</p>
																	<a href="https://support.spotify.com/" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu" data-ga-action="help"><span
																			data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Support</span></a><a
																		href="https://www.spotify.com/ca-en/download/" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu" data-ga-action="free"><span
																			data-encore-id="type" class="Type__TypeElement-sc-goli3j-0 gxaBVX">Free Mobile
																			App</span></a>
																</ul>
															</div>
															<div class="sc-fHjqPf fzcUDM">
																<ul role="list" class="TypeList__TypeListElement-sc-1jhixr6-0 nboVZ sc-hzhJZQ ibchEK"
																	data-encore-id="typeList">
																	<p data-encore-id="type" class="Type__TypeElement-sc-goli3j-0 kMPYEq">Spotify Plans
																	</p><a
																		href="https://www.spotify.com/ca-en/premium/#ref=spotifycom_footer_premium_individual"
																		role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu"
																		data-ga-action="premium-individual-footer"><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Premium Individual</span></a><a
																		href="https://www.spotify.com/ca-en/duo/#ref=spotifycom_footer_premium_duo"
																		role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu"
																		data-ga-action="premium-duo-footer"><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Premium Duo</span></a><a
																		href="https://www.spotify.com/ca-en/family/#ref=spotifycom_footer_premium_family"
																		role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu"
																		data-ga-action="premium-family-footer"><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Premium Family</span></a><a
																		href="https://www.spotify.com/ca-en/student/#ref=spotifycom_footer_premium_student"
																		role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu"
																		data-ga-action="premium-student-footer"><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Premium Student</span></a><a
																		href="https://www.spotify.com/ca-en/free/#ref=spotifycom_footer_free" role="link"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone encore-text-marginal-bold e-9911-app-footer-link sc-hmdomO dEMXNG"
																		data-encore-id="textLink" data-ga-category="menu"
																		data-ga-action="premium-free-footer"><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 gxaBVX">Spotify Free</span></a>
																</ul>
															</div>
														</div>
														<div class="sc-eBMEME hzPNiy">
															<div class="sc-dCFHLb gbrRSO"><a href="https://instagram.com/spotify"
																	aria-label="Instagram" title="Instagram" target="_blank" rel="noopener noreferrer"
																	type="button" data-encore-id="buttonIcon"
																	class="Button-sc-me270r-0 iUHXuf e-9911-button-icon sc-cWSHoV ieMOQX encore-dark-theme encore-layout-themes"><svg
																		data-encore-id="icon" role="img" aria-hidden="true"
																		class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
																		style="--encore-icon-fill: var(--text-base, #000000); --encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
																		<path
																			d="M8 1.44c2.136 0 2.389.009 3.233.047.78.036 1.203.166 1.485.276.348.128.663.332.921.598.266.258.47.573.599.921.11.282.24.706.275 1.485.039.844.047 1.097.047 3.233s-.008 2.389-.047 3.232c-.035.78-.166 1.204-.275 1.486a2.654 2.654 0 0 1-1.518 1.518c-.282.11-.706.24-1.486.275-.843.039-1.097.047-3.233.047s-2.39-.008-3.232-.047c-.78-.035-1.204-.165-1.486-.275a2.477 2.477 0 0 1-.921-.599 2.477 2.477 0 0 1-.599-.92c-.11-.282-.24-.706-.275-1.486-.038-.844-.047-1.096-.047-3.232s.009-2.39.047-3.233c.036-.78.166-1.203.275-1.485.129-.348.333-.663.599-.921a2.49 2.49 0 0 1 .92-.599c.283-.11.707-.24 1.487-.275.843-.038 1.096-.047 3.232-.047L8 1.441zm.001-1.442c-2.172 0-2.445.01-3.298.048-.854.04-1.435.176-1.943.373a3.928 3.928 0 0 0-1.417.923c-.407.4-.722.883-.923 1.417-.198.508-.333 1.09-.372 1.942C.01 5.552 0 5.826 0 8c0 2.172.01 2.445.048 3.298.04.853.174 1.433.372 1.941.2.534.516 1.017.923 1.417.4.407.883.722 1.417.923.508.198 1.09.333 1.942.372.852.039 1.126.048 3.299.048 2.172 0 2.445-.01 3.298-.048.853-.04 1.433-.174 1.94-.372a4.087 4.087 0 0 0 2.34-2.34c.199-.508.334-1.09.373-1.942.039-.851.048-1.125.048-3.298s-.01-2.445-.048-3.298c-.04-.853-.174-1.433-.372-1.94a3.924 3.924 0 0 0-.923-1.418A3.928 3.928 0 0 0 13.24.42c-.508-.197-1.09-.333-1.942-.371-.851-.041-1.125-.05-3.298-.05l.001-.001z">
																		</path>
																		<path
																			d="M8 3.892a4.108 4.108 0 1 0 0 8.216 4.108 4.108 0 0 0 0-8.216zm0 6.775a2.668 2.668 0 1 1 0-5.335 2.668 2.668 0 0 1 0 5.335zm4.27-5.978a.96.96 0 1 0 0-1.92.96.96 0 0 0 0 1.92z">
																		</path>
																	</svg></a></div>
															<div class="sc-dCFHLb gbrRSO"><a href="https://twitter.com/spotify" aria-label="Twitter"
																	title="Twitter" target="_blank" rel="noopener noreferrer" type="button"
																	data-encore-id="buttonIcon"
																	class="Button-sc-me270r-0 iUHXuf e-9911-button-icon sc-cWSHoV ieMOQX encore-dark-theme encore-layout-themes"><svg
																		data-encore-id="icon" role="img" aria-hidden="true"
																		class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
																		style="--encore-icon-fill: var(--text-base, #000000); --encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
																		<path
																			d="M13.54 3.889a2.968 2.968 0 0 0 1.333-1.683 5.937 5.937 0 0 1-1.929.738 2.992 2.992 0 0 0-.996-.706 2.98 2.98 0 0 0-1.218-.254 2.92 2.92 0 0 0-2.143.889 2.929 2.929 0 0 0-.889 2.15c0 .212.027.442.08.691a8.475 8.475 0 0 1-3.484-.932A8.536 8.536 0 0 1 1.532 2.54a2.993 2.993 0 0 0-.413 1.523c0 .519.12 1 .361 1.445.24.445.57.805.988 1.08a2.873 2.873 0 0 1-1.373-.374v.04c0 .725.23 1.365.69 1.92a2.97 2.97 0 0 0 1.739 1.048 2.937 2.937 0 0 1-1.365.056 2.94 2.94 0 0 0 1.063 1.5 2.945 2.945 0 0 0 1.77.603 5.944 5.944 0 0 1-3.77 1.302c-.243 0-.484-.016-.722-.048A8.414 8.414 0 0 0 5.15 14c.905 0 1.763-.12 2.572-.361.81-.24 1.526-.57 2.147-.988a9.044 9.044 0 0 0 1.683-1.46c.5-.556.911-1.155 1.234-1.798a9.532 9.532 0 0 0 .738-1.988 8.417 8.417 0 0 0 .246-2.429 6.177 6.177 0 0 0 1.508-1.563c-.56.249-1.14.407-1.738.476z">
																		</path>
																	</svg></a></div>
															<div class="sc-dCFHLb gbrRSO"><a href="https://www.facebook.com/Spotify"
																	aria-label="Facebook" title="Facebook" target="_blank" rel="noopener noreferrer"
																	type="button" data-encore-id="buttonIcon"
																	class="Button-sc-me270r-0 kOQsuv e-9911-button-icon sc-cWSHoV ieMOQX encore-dark-theme encore-layout-themes"><svg
																		data-encore-id="icon" role="img" aria-hidden="true"
																		class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
																		style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
																		<path
																			d="M16 8a8 8 0 1 0-9.25 7.903v-5.59H4.719V8H6.75V6.237c0-2.005 1.194-3.112 3.022-3.112.875 0 1.79.156 1.79.156V5.25h-1.008c-.994 0-1.304.617-1.304 1.25V8h2.219l-.355 2.313H9.25v5.59A8.002 8.002 0 0 0 16 8z">
																		</path>
																	</svg></a></div>
														</div>
													</div>
													<hr class="HorizontalRule__HorizontalRuleElement-sc-198gjx4-0 gPhSUm sc-tagGq csQCMv"
														data-encore-id="horizontalRule">
													<div class="sc-esYiGF ckXpPy">
														<div class="sc-iHGNWf kAjyJA">
															<div class="sc-bmzYkS iLJbxB">
																<div class="sc-jsJBEP iCKNKM"><a href="https://www.spotify.com/ca-en/legal/"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone sc-bXCLTC iajOLE"
																		data-encore-id="textLink" id=""><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 ddIxQM">Legal</span></a></div>
																<div class="sc-jsJBEP iCKNKM"><a href="https://www.spotify.com/ca-en/safetyandprivacy/"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone sc-bXCLTC iajOLE"
																		data-encore-id="textLink" id=""><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 ddIxQM">Safety &amp; Privacy
																			Center</span></a></div>
																<div class="sc-jsJBEP iCKNKM"><a
																		href="https://www.spotify.com/ca-en/legal/privacy-policy/"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone sc-bXCLTC iajOLE"
																		data-encore-id="textLink" id=""><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 ddIxQM">Privacy Policy</span></a></div>
																<div class="sc-jsJBEP iCKNKM"><a
																		href="https://www.spotify.com/ca-en/legal/cookies-policy/"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone sc-bXCLTC iajOLE"
																		data-encore-id="textLink" id=""><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 ddIxQM">Cookies</span></a></div>
																<div class="sc-jsJBEP iCKNKM"><a
																		href="https://www.spotify.com/ca-en/legal/privacy-policy/#s3"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone sc-bXCLTC iajOLE"
																		data-encore-id="textLink" id=""><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 ddIxQM">About Ads</span></a></div>
																<div class="sc-jsJBEP iCKNKM"><a href="https://www.spotify.com/ca-en/accessibility/"
																		class="e-9911-text-link e-9911-baseline encore-internal-color-text-subdued e-9911-text-link--standalone sc-bXCLTC iajOLE"
																		data-encore-id="textLink" id=""><span data-encore-id="type"
																			class="Type__TypeElement-sc-goli3j-0 ddIxQM">Accessibility</span></a></div>
															</div>
														</div>
														<div class="sc-dtBdUo jgJZhT">
															<div class="sc-kOPcWz leFkJA">
																<p data-encore-id="type" class="Type__TypeElement-sc-goli3j-0 ddIxQM">© 2025 Spotify AB
																</p>
															</div>
														</div>
													</div>
												</nav>
											</div>
										</div>
									</main>
								</div>
							</div>
							<div
								class="os-scrollbar os-scrollbar-horizontal os-theme-spotify os-scrollbar-auto-hide os-scrollbar-handle-interactive os-scrollbar-track-interactive os-scrollbar-cornerless os-scrollbar-unusable"
								style="--os-viewport-percent: 1; --os-scroll-direction: 0;">
								<div class="os-scrollbar-track">
									<div class="os-scrollbar-handle"></div>
								</div>
							</div>
							<div
								class="os-scrollbar os-scrollbar-vertical os-theme-spotify os-scrollbar-auto-hide os-scrollbar-handle-interactive os-scrollbar-track-interactive os-scrollbar-cornerless os-scrollbar-visible"
								style="--os-viewport-percent: 0.333; --os-scroll-direction: 0;">
								<div class="os-scrollbar-track">
									<div class="os-scrollbar-handle"></div>
								</div>
							</div>
						</div>
						<div>
							<div style="display: none;">
								<div class="VideoPlayer__container"></div>
							</div>
						</div>
					</div>
				</div>
				<div class="OTfMDdomT5S7B5dbYTT8">
					<div class="XOawmCGZcQx4cesyNfVO" style="width: 280px;">
						<aside aria-label="Now playing view" class="ffFwfKcPDbmAPLXzxzKq NowPlayingView enter-done"
							id="Desktop_PanelContainer_Id" tabindex="-1"
							style="--section-background-base: var(--background-elevated-base); --section-padding: 16px; --section-border-radius: 8px;">
							<div class="AAdBM1nhG73supMfnYX7">
								<div class="W3E0IT3_STcazjTeyOJa">
									<div class="fNXmHtlrj4UVWmhQrJ_5 yvZooOj0rpfRS__cAUCo KILnOHUdx4pspVEoJ7kq"><button tabindex="0"
											class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only rkIl3GXeAGoK2gIX2zuj"
											aria-label="Hide Now Playing view" aria-hidden="false" data-encore-id="buttonTertiary"><span
												aria-hidden="true" class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img"
													aria-hidden="true" class="e-9911-icon e-9911-baseline e-9911-icon--auto-mirror"
													viewBox="0 0 16 16"
													style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
													<path
														d="M10.03 10.53a.75.75 0 1 1-1.06-1.06L10.44 8 8.97 6.53a.75.75 0 0 1 1.06-1.06l2 2a.75.75 0 0 1 0 1.06l-2 2Z">
													</path>
													<path
														d="M15 16a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h14Zm-8.5-1.5v-13h8v13h-8Zm-1.5 0H1.5v-13H5v13Z">
													</path>
												</svg></span></button>
										<div class="eTT681T6oUKXsIMiP8pT k_ndsg7yz9ZAgEmei1n3 j9Ey7DzF10wbxpBIVtcb"><a draggable="true"
												class="gwmgu53xszgwAXxqLT0h"
												href="/track/3g3GjHuxntUfUd4t23rGTZ?uid=c657f3f962dbf2a63372&amp;uri=spotify:track:3g3GjHuxntUfUd4t23rGTZ">
												<div class="eSMjmiD29Ox35O95waw6"><span class="cpltqpeZsQmmXy7qZgb9"><span
															class="PGSe59fD1Hwc9yUM2d3U" style="--marquee-width: 146px;">
															<h1 class="e-9911-text encore-text-body-medium-bold encore-internal-color-text-base"
																data-encore-id="text" dir="auto">Cool</h1>
														</span></span></div>
											</a></div><span class="icNf66tgG3uxDMbCCIaN XOSSUjLDKk9RRmiX_UWa">
											<div class="UAg2mNxhAm_jv0zFjG8z"><button aria-haspopup="menu" data-testid="more-button"
													class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only wPHL366l99aluPsMU8Bl"
													aria-label="More options for Cool" data-encore-id="buttonTertiary"><span aria-hidden="true"
														class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
															class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
															style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
															<path
																d="M3 8a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm6.5 0a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zM16 8a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z">
															</path>
														</svg></span></button><button
													class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only wPHL366l99aluPsMU8Bl"
													aria-label="Expand Now Playing view" data-encore-id="buttonTertiary"><span aria-hidden="true"
														class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
															class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
															style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
															<path
																d="M6.53 9.47a.75.75 0 0 1 0 1.06l-2.72 2.72h1.018a.75.75 0 0 1 0 1.5H1.25v-3.579a.75.75 0 0 1 1.5 0v1.018l2.72-2.72a.75.75 0 0 1 1.06 0zm2.94-2.94a.75.75 0 0 1 0-1.06l2.72-2.72h-1.018a.75.75 0 1 1 0-1.5h3.578v3.579a.75.75 0 0 1-1.5 0V3.81l-2.72 2.72a.75.75 0 0 1-1.06 0z">
															</path>
														</svg></span></button></div>
										</span>
									</div>
								</div>
								<div data-overlayscrollbars-initialize="true" class="cZCuJDjrGA2QMXja_Sua ZjfaJlGQZ42nCWjD3FDm"
									data-overlayscrollbars="host">
									<div class="" data-overlayscrollbars-viewport="scrollbarHidden overflowXHidden overflowYScroll"
										tabindex="-1"
										style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; top: 0px; right: auto; left: 0px; width: calc(100% + 0px); padding: 0px;">
										<div class="AAdBM1nhG73supMfnYX7 zduvaX0Ioxqd5ypeWoAf IkRGajTjItEFQkRMeH6v">
											<div class="nw2W4ZMdICuBo08Tzxg9" data-testid="NPV_Panel_OpenDiv">
												<div class="fIpDXK7M3W0Bn3FgLSRe">
													<div class="cIUedsmg_cTnTxvOYTKR">
														<div class="zL6hQR4mukVUUQaa_7K1 hjyiWzPtKHn_5kCe9vyg pUIBQ9cykHKYx2A2ZIPA">
															<div class="ylBRlfNqGnzVa4kjUQGP _q9LkNJJIpxoOkOFI2Nd" aria-hidden="true"
																data-testid="track-visual-enhancement">
																<div draggable="true" class="URfgKDbFQpKuN8ZjGdui"><a draggable="false"
																		data-testid="context-link" data-context-item-type="track"
																		aria-label="Now playing: Cool by Daniel Caesar"
																		href="/album/7ivbFszr1TbVadj89BIy1y?uid=c657f3f962dbf2a63372&amp;uri=spotify%3Atrack%3A3g3GjHuxntUfUd4t23rGTZ"
																		style="border: none;">
																		<div class="j9I5h3Z4o0fKNgI1fIjb">
																			<div class="H0HbpIM3UrcupWIAjLWu W0TACB7OY0iXtKVOtEhY" aria-hidden="true">
																				<div class="zmOtW0vqqn1qpZrtQ_w9"><svg data-encore-id="icon" role="img"
																						aria-hidden="true" class="e-9911-icon e-9911-baseline" data-testid="track"
																						viewBox="0 0 24 24">
																						<path
																							d="M6 3h15v15.167a3.5 3.5 0 1 1-3.5-3.5H19V5H8v13.167a3.5 3.5 0 1 1-3.5-3.5H6V3zm0 13.667H4.5a1.5 1.5 0 1 0 1.5 1.5v-1.5zm13 0h-1.5a1.5 1.5 0 1 0 1.5 1.5v-1.5z">
																						</path>
																					</svg></div><img aria-hidden="false" draggable="false" loading="eager"
																					src="https://i.scdn.co/image/ab67616d0000b2737c68face1dc58127f3a7b1cc"
																					data-testid="cover-art-image" alt=""
																					class="mMx2LUixlnN_Fu45JpFB FqmFsMhuF4D0s35Z62Js Yn2Ei5QZn19gria6LjZj">
																			</div>
																		</div>
																	</a></div>
															</div>
															<div class="E08D6ucrHuPJYzzGO7HG" aria-hidden="true">
																<div draggable="true">
																	<div class="canvasVideoContainerNPV huMHH_FySIW5UhSrJfy8"><video playsinline=""
																			loop="" src="blob:https://open.spotify.com/822afe01-bfd6-42e2-a76c-b68171f88f81"
																			crossorigin="anonymous"></video></div>
																</div>
															</div>
															<div id="VideoPlayerNpv_ReactPortal" class="KrBYgWLGb5aRHjoD_prX"></div>
														</div>
														<div class="aaFQbW0j0N40v_siz0kX bLX5l9C_iEfonbMKiFD_">
															<div class="KHaAkbA62j5I7pcLsDAx" data-testid="minimized-track-visual-enhancement">
																<div draggable="true"><a draggable="false" data-testid="context-link"
																		data-context-item-type="track" aria-label="Now playing: Cool by Daniel Caesar"
																		href="/album/7ivbFszr1TbVadj89BIy1y?uid=c657f3f962dbf2a63372&amp;uri=spotify%3Atrack%3A3g3GjHuxntUfUd4t23rGTZ"
																		style="border: none;">
																		<div class="jKvr1cqkZZXpH5z92z9b peN_VMHSmvTVUx9rneyY">
																			<div class="H0HbpIM3UrcupWIAjLWu W0TACB7OY0iXtKVOtEhY" aria-hidden="true">
																				<div class="zmOtW0vqqn1qpZrtQ_w9"><svg data-encore-id="icon" role="img"
																						aria-hidden="true" class="e-9911-icon e-9911-baseline" data-testid="track"
																						viewBox="0 0 24 24">
																						<path
																							d="M6 3h15v15.167a3.5 3.5 0 1 1-3.5-3.5H19V5H8v13.167a3.5 3.5 0 1 1-3.5-3.5H6V3zm0 13.667H4.5a1.5 1.5 0 1 0 1.5 1.5v-1.5zm13 0h-1.5a1.5 1.5 0 1 0 1.5 1.5v-1.5z">
																						</path>
																					</svg></div><img aria-hidden="false" draggable="false" loading="eager"
																					src="https://i.scdn.co/image/ab67616d000048517c68face1dc58127f3a7b1cc"
																					data-testid="cover-art-image" alt=""
																					class="mMx2LUixlnN_Fu45JpFB FqmFsMhuF4D0s35Z62Js Yn2Ei5QZn19gria6LjZj">
																			</div>
																		</div>
																	</a></div>
															</div>
															<div class="hfdkySA4kiUldFsPj9lD iZrIHsls0lCEhoMDA9kc">
																<div class="PcH6VnzkkDqD36P93i9Q">
																	<div class="eSMjmiD29Ox35O95waw6"><span class="cpltqpeZsQmmXy7qZgb9"><span
																				class="PGSe59fD1Hwc9yUM2d3U" style="--marquee-width: 226px;">
																				<div class="e-9911-text encore-text-title-small K9Nj3oI7bTNFh5AGp5GA"
																					data-encore-id="text" data-testid="context-item-info-title" dir="auto"><span
																						draggable="true"><a draggable="false" data-testid="context-item-link"
																							href="/album/7ivbFszr1TbVadj89BIy1y">Cool</a></span></div>
																			</span></span></div>
																</div>
																<div class="p2ya1fQ3o9pY4alcW0o4"></div>
																<div class="w_TTPh4y9H1YD6UrTMHa">
																	<div class="eSMjmiD29Ox35O95waw6"><span class="cpltqpeZsQmmXy7qZgb9"><span
																				class="PGSe59fD1Hwc9yUM2d3U" style="--marquee-width: 112px;">
																				<div
																					class="e-9911-text encore-text-body-medium encore-internal-color-text-subdued w_TTPh4y9H1YD6UrTMHa"
																					data-encore-id="text" data-testid="context-item-info-subtitles"><span><a
																							draggable="true" data-testid="context-item-info-artist" dir="auto"
																							href="/artist/20wkVLutqVOYrc0kxFs7rA">Daniel Caesar</a></span></div>
																			</span></span></div>
																</div>
															</div><button tabindex="0"
																class="Button-sc-1dqy6lx-0 deFNvm e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only e-9911-button-tertiary--condensed pvGZ831aNzHTQMZ8CA_u DFvRASpHOFAoziM4w7En sJHheSrjFUt_MAcNrUXQ"
																aria-label="Copy Song Link" aria-hidden="false" data-encore-id="buttonTertiary"><span
																	aria-hidden="true" class="e-9911-button__icon-wrapper"><svg data-encore-id="icon"
																		role="img" aria-hidden="true" class="e-9911-icon e-9911-baseline"
																		viewBox="0 0 16 16"
																		style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
																		<path
																			d="M1 5.75A.75.75 0 0 1 1.75 5H4v1.5H2.5v8h11v-8H12V5h2.25a.75.75 0 0 1 .75.75v9.5a.75.75 0 0 1-.75.75H1.75a.75.75 0 0 1-.75-.75v-9.5z">
																		</path>
																		<path
																			d="M8 9.576a.75.75 0 0 0 .75-.75V2.903l1.454 1.454a.75.75 0 0 0 1.06-1.06L8 .03 4.735 3.296a.75.75 0 0 0 1.06 1.061L7.25 2.903v5.923c0 .414.336.75.75.75z">
																		</path>
																	</svg></span></button>
															<div class="O5NOY8Xw4NH0IhBZu8tm"><button aria-checked="true"
																	class="Button-sc-1dqy6lx-0 gDSiSh e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only e-9911-button-tertiary--condensed hhFdIYRyHsqlCHy7T_8A"
																	aria-label="Add to playlist" data-encore-id="buttonTertiary"><span aria-hidden="true"
																		class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img"
																			aria-hidden="true" class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
																			style="--encore-icon-fill: var(--text-bright-accent, #107434); --encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
																			<path
																				d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm11.748-1.97a.75.75 0 0 0-1.06-1.06l-4.47 4.47-1.405-1.406a.75.75 0 1 0-1.061 1.06l2.466 2.467 5.53-5.53z">
																			</path>
																		</svg></span></button></div>
														</div>
													</div>
												</div>
												<div class="Ai_McRq9wJEYK21w8nX_ QR9JmVmX9LYwo62NRtew"><button type="button"
														aria-label="Daniel Caesar" class="k90FaSa2GhsINq5izwhz" tabindex="0"
														data-testid="npv-artist-bio-button">
														<div class="XxNYTMMTOE82fg4VfwMu">
															<div class="Rol5Gmuk1O2tMw7NMtxF zblh0cP5LieDz0Z7_3g3 vfJEDN5R3Sh1q8XvqC4g"
																style="background-image: linear-gradient(rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0) 50%), url(&quot;https://i.scdn.co/image/ab6761670000ecd4f97510e02efb66f1b068611f&quot;);">
																<div class="BNUKh7vF7Z90gfa0YoHu">
																	<div class="EVqc6HChiM9pEqBYAiUE">
																		<h2 class="e-9911-text encore-text-body-medium-bold encore-internal-color-text-base"
																			data-encore-id="text">
																			<div class="zZdI03asKaUCNlbhjDAv">About the artist</div>
																		</h2>
																	</div>
																</div>
															</div>
															<div class="CvxzmyND_aGd2RR8ZoSr"><a data-testid="npv-artist-link"
																	href="/artist/20wkVLutqVOYrc0kxFs7rA"><span
																		class="e-9911-text encore-text-body-medium-bold" data-encore-id="text"
																		dir="auto">Daniel Caesar</span></a>
																<div class="iWpZp7Ab_9h7s_U1SsLN">
																	<div
																		class="e-9911-text encore-text-body-medium encore-internal-color-text-subdued EUZ35kQ5pEz50WCc4OwW"
																		data-encore-id="text">33,001,553 monthly listeners</div>
																	<div tabindex="0"
																		class="Button-sc-y0gtbx-0 iEnZvo encore-text-body-small-bold e-9911-button--small HfjKySFpamYeN3Ya5lZA"
																		data-encore-id="buttonSecondary">Follow</div>
																</div><span
																	class="e-9911-text encore-text-body-small encore-internal-color-text-subdued r8e3SfYjm_1JbXLXV3YP"
																	data-encore-id="text">Daniel Caesar’s first chapter unfolded in a suburb of Toronto,
																	where he was born to Bajan and Jamaican parents and raised listening to soul and
																	gospel music while singing in front of his father’s church congregation. The singer
																	and songwriter left home at 17 to pursue his calling as a musical artist. Caesar
																	independently released his first two EPs, Praise Break (2014) and Pilgrim’s Paradise
																	(2017), to widespread praise—the first of which landed at #19 on Rolling Stone’s list
																	of “20 Best R&amp;B Albums of 2014.” However, it was his 2017 debut album, Freudian,
																	that marked him as one of this generation’s most exciting artists to watch—the album
																	went on to be nominated for two GRAMMY Awards (“Best R&amp;B Album” and “Best R&amp;B
																	Performance” for “Get You”), and the following year, Caesar took home the award for
																	“Best R&amp;B Performance” for his breakout hit, “Best Part.” The GRAMMY Award-winning
																	and Juno Award-winning artist soon followed this early success with his critically
																	acclaimed sophomore album, Case Study 01 (2019), and most recently his multi-platinum,
																	worldwide hit, “Peaches” with Justin Bieber and Giveon (2021). Amassing over 5 billion
																	streams across his catalogue and over 31 million monthly listeners, Caesar currently
																	ranked the 79th “Most Listened To Artist in the World” and top 10 “Most Streamed
																	Canadian Artists of All Time” on Spotify. Now, Daniel Caesar gears up for his next
																	chapter, as he continues to redefine what R&amp;B can be, while quietly overtaking the
																	mainstream.</span>
															</div>
														</div>
													</button></div>
												<div class="Ai_McRq9wJEYK21w8nX_ l2PpoXJouAgqFCuNT3iB">
													<div class="EVqc6HChiM9pEqBYAiUE">
														<h2 class="e-9911-text encore-text-body-medium-bold encore-internal-color-text-base"
															data-encore-id="text">
															<div class="zZdI03asKaUCNlbhjDAv">Credits</div>
														</h2><button
															class="Button-sc-1dqy6lx-0 gLxfIu encore-text-body-small-bold e-9911-overflow-wrap-anywhere e-9911-button-tertiary--condensed bBldZtWu4QtzmrTfHOKm"
															data-encore-id="buttonTertiary">Show all</button>
													</div>
													<div
														class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 efnFkI Box-sc-8t9c76-0 efnFkI"
														data-encore-id="listRow" role="group"
														aria-labelledby="listrow-title-spotify:artist:20wkVLutqVOYrc0kxFs7rA"
														data-testid="credits-artist-row"
														style="--box-padding-block-start: 4px; --box-padding-block-end: 4px; --box-padding-inline-start: 0; --box-padding-inline-end: 0; --box-min-block-size: 32px;">
														<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
															<div class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM"><a
																	draggable="false" data-testid="artist-row-credits-link"
																	href="/artist/20wkVLutqVOYrc0kxFs7rA"><span
																		class="e-9911-text encore-text-body-medium" data-encore-id="text">Daniel
																		Caesar</span></a><span
																	class="e-9911-text encore-text-body-small encore-internal-color-text-subdued"
																	data-encore-id="text" data-testid="artist-row-role"
																	style="text-transform: capitalize;">Main Artist</span></div>
															<div
																class="Areas__InteractiveArea-sc-8gfrea-0 Areas__TrailingSlot-sc-8gfrea-7 bJSfgC jpzxju">
																<button
																	class="Button-sc-y0gtbx-0 iEnZvo encore-text-body-small-bold e-9911-button--small"
																	data-encore-id="buttonSecondary">Follow</button></div>
														</div>
													</div>
													<div
														class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 efnFkI Box-sc-8t9c76-0 efnFkI"
														data-encore-id="listRow" role="group"
														aria-labelledby="listrow-title-spotify:artist:1hQGslv712aGImOWuT45Vs"
														data-testid="credits-artist-row"
														style="--box-padding-block-start: 4px; --box-padding-block-end: 4px; --box-padding-inline-start: 0; --box-padding-inline-end: 0; --box-min-block-size: 32px;">
														<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
															<div class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																<span class="e-9911-text encore-text-body-medium" data-encore-id="text">Ashton
																	Simmonds</span><span
																	class="e-9911-text encore-text-body-small encore-internal-color-text-subdued"
																	data-encore-id="text" data-testid="artist-row-role"
																	style="text-transform: capitalize;">Composer, Producer</span></div>
														</div>
													</div>
													<div
														class="e-9911-box e-9911-baseline e-9911-box--naked e-9911-box--browser-default-focus e-9911-box--padding-custom e-9911-box--min-size e-9911-Box-sc-8t9c76-0 efnFkI Box-sc-8t9c76-0 efnFkI"
														data-encore-id="listRow" role="group"
														aria-labelledby="listrow-title-spotify:artist:5oq46vINX6yvYPAUaAf25x"
														data-testid="credits-artist-row"
														style="--box-padding-block-start: 4px; --box-padding-block-end: 4px; --box-padding-inline-start: 0; --box-padding-inline-end: 0; --box-min-block-size: 32px;">
														<div class="Areas__HeaderArea-sc-8gfrea-3 TJKQw">
															<div class="Areas__InteractiveArea-sc-8gfrea-0 Areas__Column-sc-8gfrea-5 bJSfgC jwUvtM">
																<span class="e-9911-text encore-text-body-medium" data-encore-id="text">Sacha
																	Rudy</span><span
																	class="e-9911-text encore-text-body-small encore-internal-color-text-subdued"
																	data-encore-id="text" data-testid="artist-row-role"
																	style="text-transform: capitalize;">Composer, Producer</span></div>
														</div>
													</div>
												</div>
												<div class="Ai_McRq9wJEYK21w8nX_ wpJvLvrrnyP0_C7hLkqg">
													<div class="EVqc6HChiM9pEqBYAiUE">
														<h2 class="e-9911-text encore-text-body-medium-bold encore-internal-color-text-base"
															data-encore-id="text">
															<div class="zZdI03asKaUCNlbhjDAv">Merch</div>
														</h2>
													</div>
													<ul>
														<li>
															<div class="RClL7GUhUo_xqzNcsXSG"><img aria-hidden="false" draggable="false"
																	loading="lazy" src="https://i.scdn.co/image/ab676d63000076a0cc52a495cf5d29a75b6b4104"
																	alt="SUPERPOWERS WORLD TOUR LOOK WHAT THEY DID TO ME BABY ZIP HOODIE"
																	class="mMx2LUixlnN_Fu45JpFB EQaztpbGtXeN7V1cjAP4 Yn2Ei5QZn19gria6LjZj" width="48"
																	height="48">
																<div class="tYSzgx8hG37WjBDn364n"><a draggable="false" target="_blank"
																		href="https://shop.spotify.com/en-gb/artist/20wkVLutqVOYrc0kxFs7rA/product/superpowers-world-tour-look-what-they-did-to-me-baby-zip-hoodie?utm_source=spotify&amp;utm_medium=app-nowplayingview&amp;utm_term=00a4665c250178c37927621b3f2617a605bc0750c6e9cceb3ff95c"
																		rel="noopener"><span
																			class="e-9911-text encore-text-body-medium encore-internal-color-text-base _4XNZPDdnyq1HHKG5Qtx"
																			data-encore-id="text" data-testid="offer-name">SUPERPOWERS WORLD TOUR LOOK WHAT
																			THEY DID TO ME BABY ZIP HOODIE</span></a>
																	<p class="e-9911-text encore-text-body-small DehN40s8150pzqyBfGN_"
																		data-encore-id="text"></p>
																</div><svg data-encore-id="icon" role="img" aria-hidden="true"
																	class="e-9911-icon e-9911-baseline ZiRNxR2_6cTTMHIqpwzl" viewBox="0 0 16 16"
																	style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
																	<path
																		d="M1 2.75A.75.75 0 0 1 1.75 2H7v1.5H2.5v11h10.219V9h1.5v6.25a.75.75 0 0 1-.75.75H1.75a.75.75 0 0 1-.75-.75V2.75z">
																	</path>
																	<path
																		d="M15 1v4.993a.75.75 0 1 1-1.5 0V3.56L8.78 8.28a.75.75 0 0 1-1.06-1.06l4.72-4.72h-2.433a.75.75 0 0 1 0-1.5H15z">
																	</path>
																</svg>
															</div>
														</li>
														<li>
															<div class="RClL7GUhUo_xqzNcsXSG"><img aria-hidden="false" draggable="false"
																	loading="lazy" src="https://i.scdn.co/image/ab676d63000076a00e5e782678e7f44afe549912"
																	alt="SUPERPOWERS WORLD TOUR LEG 3 TEE (BLACK)"
																	class="mMx2LUixlnN_Fu45JpFB EQaztpbGtXeN7V1cjAP4 Yn2Ei5QZn19gria6LjZj" width="48"
																	height="48">
																<div class="tYSzgx8hG37WjBDn364n"><a draggable="false" target="_blank"
																		href="https://shop.spotify.com/en-gb/artist/20wkVLutqVOYrc0kxFs7rA/product/superpowers-world-tour-leg-3-tee-black?utm_source=spotify&amp;utm_medium=app-nowplayingview&amp;utm_term=00a4665c250178c37927621b3f2617a605bc0750c6e9cceb3ff95c"
																		rel="noopener"><span
																			class="e-9911-text encore-text-body-medium encore-internal-color-text-base _4XNZPDdnyq1HHKG5Qtx"
																			data-encore-id="text" data-testid="offer-name">SUPERPOWERS WORLD TOUR LEG 3 TEE
																			(BLACK)</span></a>
																	<p class="e-9911-text encore-text-body-small DehN40s8150pzqyBfGN_"
																		data-encore-id="text"></p>
																</div><svg data-encore-id="icon" role="img" aria-hidden="true"
																	class="e-9911-icon e-9911-baseline ZiRNxR2_6cTTMHIqpwzl" viewBox="0 0 16 16"
																	style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
																	<path
																		d="M1 2.75A.75.75 0 0 1 1.75 2H7v1.5H2.5v11h10.219V9h1.5v6.25a.75.75 0 0 1-.75.75H1.75a.75.75 0 0 1-.75-.75V2.75z">
																	</path>
																	<path
																		d="M15 1v4.993a.75.75 0 1 1-1.5 0V3.56L8.78 8.28a.75.75 0 0 1-1.06-1.06l4.72-4.72h-2.433a.75.75 0 0 1 0-1.5H15z">
																	</path>
																</svg>
															</div>
														</li>
														<li>
															<div class="RClL7GUhUo_xqzNcsXSG"><img aria-hidden="false" draggable="false"
																	loading="lazy" src="https://i.scdn.co/image/ab676d63000076a0dc8b39d1ee80fa16117bf5ca"
																	alt="SUPERPOWERS WORLD TOUR PAIN IS INEVITABLE CROPPED THERMAL LONGSLEEVE"
																	class="mMx2LUixlnN_Fu45JpFB EQaztpbGtXeN7V1cjAP4 Yn2Ei5QZn19gria6LjZj" width="48"
																	height="48">
																<div class="tYSzgx8hG37WjBDn364n"><a draggable="false" target="_blank"
																		href="https://shop.spotify.com/en-gb/artist/20wkVLutqVOYrc0kxFs7rA/product/superpowers-world-tour-cropped-thermal-longsleeve?utm_source=spotify&amp;utm_medium=app-nowplayingview&amp;utm_term=00a4665c250178c37927621b3f2617a605bc0750c6e9cceb3ff95c"
																		rel="noopener"><span
																			class="e-9911-text encore-text-body-medium encore-internal-color-text-base _4XNZPDdnyq1HHKG5Qtx"
																			data-encore-id="text" data-testid="offer-name">SUPERPOWERS WORLD TOUR PAIN IS
																			INEVITABLE CROPPED THERMAL LONGSLEEVE</span></a>
																	<p class="e-9911-text encore-text-body-small DehN40s8150pzqyBfGN_"
																		data-encore-id="text"></p>
																</div><svg data-encore-id="icon" role="img" aria-hidden="true"
																	class="e-9911-icon e-9911-baseline ZiRNxR2_6cTTMHIqpwzl" viewBox="0 0 16 16"
																	style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
																	<path
																		d="M1 2.75A.75.75 0 0 1 1.75 2H7v1.5H2.5v11h10.219V9h1.5v6.25a.75.75 0 0 1-.75.75H1.75a.75.75 0 0 1-.75-.75V2.75z">
																	</path>
																	<path
																		d="M15 1v4.993a.75.75 0 1 1-1.5 0V3.56L8.78 8.28a.75.75 0 0 1-1.06-1.06l4.72-4.72h-2.433a.75.75 0 0 1 0-1.5H15z">
																	</path>
																</svg>
															</div>
														</li>
													</ul>
												</div>
												<div class="Ai_McRq9wJEYK21w8nX_ qbOrWcMUhSri1nPkZLQA" style="--section-gap: 8px;">
													<div class="EVqc6HChiM9pEqBYAiUE">
														<h2 class="e-9911-text encore-text-body-medium-bold encore-internal-color-text-base"
															data-encore-id="text">
															<div class="zZdI03asKaUCNlbhjDAv">Your queue is empty</div>
														</h2>
													</div><a draggable="false" href="/search"><button
															class="Button-sc-y0gtbx-0 iEnZvo encore-text-body-small-bold e-9911-button--small ButtonSecondary___StyledEncoreButtonSecondary-sc-13xoveo-0 kQFuGw"
															data-encore-id="buttonSecondary">Search for something new</button></a>
												</div>
											</div>
										</div>
									</div>
									<div
										class="os-scrollbar os-scrollbar-horizontal os-theme-spotify os-scrollbar-auto-hide os-scrollbar-auto-hide-hidden os-scrollbar-handle-interactive os-scrollbar-track-interactive os-scrollbar-cornerless os-scrollbar-unusable"
										style="--os-viewport-percent: 1; --os-scroll-direction: 0;">
										<div class="os-scrollbar-track">
											<div class="os-scrollbar-handle"></div>
										</div>
									</div>
									<div
										class="os-scrollbar os-scrollbar-vertical os-theme-spotify os-scrollbar-auto-hide os-scrollbar-auto-hide-hidden os-scrollbar-handle-interactive os-scrollbar-track-interactive os-scrollbar-visible os-scrollbar-cornerless"
										style="--os-viewport-percent: 0.49; --os-scroll-direction: 0;">
										<div class="os-scrollbar-track">
											<div class="os-scrollbar-handle"></div>
										</div>
									</div>
								</div>
							</div>
						</aside>
					</div>
					<div data-testid="LayoutResizer__resize-bar" class="LayoutResizer__resize-bar LayoutResizer__inline-start">
						<label class="hidden-visually">Resize main navigation<input class="LayoutResizer__input" type="range"
								min="280" max="280" step="10" value="280"></label></div>
				</div>
				<div id="lyrics-cinema" class="Root__lyrics-cinema"></div>
				<div class="xlgKfueiF46Wo_sED8YA mMjg1Gizg9kYk8ILoTdp"
					style="grid-area: global-nav / left-sidebar / main-view / right-sidebar; z-index: var(--above-everything-except-now-playing-bar-z-index);">
				</div>
				<div class="xlgKfueiF46Wo_sED8YA mMjg1Gizg9kYk8ILoTdp"
					style="grid-area: global-nav / left-sidebar / main-view / right-sidebar; z-index: var(--above-everything-except-now-playing-bar-z-index);">
				</div>
				<div class="xlgKfueiF46Wo_sED8YA"
					style="grid-area: main-view / left-sidebar / main-view / main-view; z-index: var(--above-main-and-now-playing-view-grid-area-z-index);">
					<div class="VTO__modal-slot"></div>
				</div>
				<div class="xlgKfueiF46Wo_sED8YA"
					style="grid-area: global-nav / left-sidebar / now-playing-bar / right-sidebar; z-index: var(--above-everything-grid-area-z-index);">
				</div>
				<div class="xlgKfueiF46Wo_sED8YA"
					style="grid-area: global-nav / left-sidebar / now-playing-bar / right-sidebar; z-index: var(--above-everything-grid-area-z-index);">
					<div id="floating-ui-popover-layer" style="z-index: 1;"></div>
				</div>
			</div>
			<div>
				<div>
					<div data-testid="language-selection-modal" class="KPuW9eE4auKgVgMtPZoH" role="presentation">
						<div class="qzuG9AHNXHQrOGF06r9A" role="dialog" hidden="" aria-modal="true"
							aria-labelledby="language-selection-title" aria-describedby="language-selection-subtitle">
							<div class="ZgjCz5A7qOyprtvcLK8y">
								<div class="BSwvSvqHiQUVuim4Eidv">
									<h1 class="e-9911-text encore-text-title-small encore-internal-color-text-base" data-encore-id="text"
										id="language-selection-title" style="padding-block-end: 8px;">Choose a language</h1>
									<p class="e-9911-text encore-text-body-medium encore-internal-color-text-base" data-encore-id="text"
										id="language-selection-subtitle" style="padding-block-end: 16px;">This updates what you read on
										open.spotify.com</p>
								</div><button data-testid="close-button" class="TpluDuF12UKv3IIq_VDu"><svg data-encore-id="icon"
										role="img" aria-label="Close" aria-hidden="false" class="e-9911-icon e-9911-baseline"
										viewBox="0 0 16 16"
										style="--encore-icon-height: var(--encore-graphic-size-informative-smaller); --encore-icon-width: var(--encore-graphic-size-informative-smaller);">
										<path
											d="M2.47 2.47a.75.75 0 0 1 1.06 0L8 6.94l4.47-4.47a.75.75 0 1 1 1.06 1.06L9.06 8l4.47 4.47a.75.75 0 1 1-1.06 1.06L8 9.06l-4.47 4.47a.75.75 0 0 1-1.06-1.06L6.94 8 2.47 3.53a.75.75 0 0 1 0-1.06Z">
										</path>
									</svg></button>
							</div>
							<div class="eYLSfS4EKfwsdTsItWkY" style="--header-height: undefinedpx;"><button
									class="ZpqHX3kvsJIsR1QIc4kf" id="en" data-testid="language-option-en"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">English</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">English</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="af"
									data-testid="language-option-af"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Afrikaans</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Afrikaans</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="am"
									data-testid="language-option-am"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">አማርኛ</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Amharic</span></button><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="ar"
									data-testid="language-option-ar"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">العَرَبِيَّة</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Arabic</span></a><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="ar-EG"
									data-testid="language-option-ar-EG"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">عربي مصري</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Arabic (Egypt)</span></a><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="ar-MA"
									data-testid="language-option-ar-MA"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">العَرَبِيَّة مغربي</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Arabic (Morocco)</span></a><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="ar-SA"
									data-testid="language-option-ar-SA"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">العربية السعودية</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Arabic (Saudi Arabia)</span></a><button class="ZpqHX3kvsJIsR1QIc4kf" id="az"
									data-testid="language-option-az"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Azərbaycanca</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Azerbaijani</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="bg"
									data-testid="language-option-bg"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Български</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Bulgarian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="bho"
									data-testid="language-option-bho"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">भोजपुरी</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Bhojpuri</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="bn"
									data-testid="language-option-bn"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">বাংলা</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Bengali</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="bs"
									data-testid="language-option-bs"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Bosanski</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Bosnian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="ca"
									data-testid="language-option-ca"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Català</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Catalan</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="cs"
									data-testid="language-option-cs"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Čeština</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Czech</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="da"
									data-testid="language-option-da"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Dansk</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Danish</span></button><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="de"
									data-testid="language-option-de"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Deutsch</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">German</span></a><button class="ZpqHX3kvsJIsR1QIc4kf" id="el"
									data-testid="language-option-el"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Eλληνικά</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Greek</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="en-GB"
									data-testid="language-option-en-GB"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">English</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">United Kingdom</span></button><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="es"
									data-testid="language-option-es"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Español de España</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">European Spanish</span></a><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf"
									id="es-419" data-testid="language-option-es-419"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Español de Latinoamérica</span><span
										class="e-9911-text encore-text-body-medium" data-encore-id="text">Latin American
										Spanish</span></a><a href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu"
									class="ZpqHX3kvsJIsR1QIc4kf" id="es-AR" data-testid="language-option-es-AR"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Español (Argentina)</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Spanish (Argentina)</span></a><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="es-MX"
									data-testid="language-option-es-MX"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Español (México)</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Spanish (Mexico)</span></a><button class="ZpqHX3kvsJIsR1QIc4kf" id="et"
									data-testid="language-option-et"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Eesti</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Estonian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="eu"
									data-testid="language-option-eu"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Euskara</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Basque</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="fa"
									data-testid="language-option-fa"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">فارسی</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Persian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="fi"
									data-testid="language-option-fi"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Suomeksi</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Finnish</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="fil"
									data-testid="language-option-fil"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Filipino</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Filipino</span></button><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="fr"
									data-testid="language-option-fr"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Français</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">French</span></a><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="fr-CA"
									data-testid="language-option-fr-CA"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Français Canadien</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Canadian French</span></a><button class="ZpqHX3kvsJIsR1QIc4kf" id="gl"
									data-testid="language-option-gl"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Galego</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Galician</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="gu"
									data-testid="language-option-gu"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">ગુજરાતી</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Gujarati</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="he"
									data-testid="language-option-he"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">עברית</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Hebrew</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="hi"
									data-testid="language-option-hi"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">हिन्दी</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Hindi</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="hr"
									data-testid="language-option-hr"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Hrvatski</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Croatian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="hu"
									data-testid="language-option-hu"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Magyar</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Hungarian</span></button><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="id"
									data-testid="language-option-id"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Bahasa Indonesia</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Indonesian</span></a><button class="ZpqHX3kvsJIsR1QIc4kf" id="is"
									data-testid="language-option-is"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Íslenska</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Icelandic</span></button><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="it"
									data-testid="language-option-it"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Italiano</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Italian</span></a><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="ja"
									data-testid="language-option-ja"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">日本語</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Japanese</span></a><button class="ZpqHX3kvsJIsR1QIc4kf" id="kn"
									data-testid="language-option-kn"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">ಕನ್ನಡ</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Kannada</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="ko"
									data-testid="language-option-ko"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">한국어</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Korean</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="lt"
									data-testid="language-option-lt"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Lietuvių</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Lithuanian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="lv"
									data-testid="language-option-lv"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Latviešu</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Latvian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="mk"
									data-testid="language-option-mk"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Македонски</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Macedonian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="ml"
									data-testid="language-option-ml"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">മലയാളം</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Malayalam</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="mr"
									data-testid="language-option-mr"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">मराठी</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Marathi</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="ms"
									data-testid="language-option-ms"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Melayu</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Malay</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="nb"
									data-testid="language-option-nb"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Norsk</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Norwegian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="ne"
									data-testid="language-option-ne"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">नेपाली</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Nepali</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="nl"
									data-testid="language-option-nl"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Nederlands</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Dutch</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="or"
									data-testid="language-option-or"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">ଓଡ଼ିଆ</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Odia</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="pa-IN"
									data-testid="language-option-pa-IN"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">ਪੰਜਾਬੀ</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Punjabi</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="pa-PK"
									data-testid="language-option-pa-PK"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">پنجابی</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Punjabi (Naskh)</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="pl"
									data-testid="language-option-pl"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Polski</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Polish</span></button><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="pt-BR"
									data-testid="language-option-pt-BR"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Português do Brasil</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Brazilian Portuguese</span></a><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="pt-PT"
									data-testid="language-option-pt-PT"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Português</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">European Portuguese</span></a><button class="ZpqHX3kvsJIsR1QIc4kf" id="ro"
									data-testid="language-option-ro"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Română</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Romanian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="ru"
									data-testid="language-option-ru"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Русский</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Russian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="sk"
									data-testid="language-option-sk"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Slovenčina</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Slovak</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="sl"
									data-testid="language-option-sl"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Slovenski</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Slovenian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="sr"
									data-testid="language-option-sr"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Srpski</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Serbian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="sv"
									data-testid="language-option-sv"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Svenska</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Swedish</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="sw"
									data-testid="language-option-sw"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Kiswahili</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Swahili</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="ta"
									data-testid="language-option-ta"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">தமிழ்</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Tamil</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="te"
									data-testid="language-option-te"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">తెలుగు</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Telugu</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="th"
									data-testid="language-option-th"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">ภาษาไทย</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Thai</span></button><a
									href="https://open.spotify.com/user/kw1zwmvfczcvnf03b9h3rxnzu" class="ZpqHX3kvsJIsR1QIc4kf" id="tr"
									data-testid="language-option-tr"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Türkçe</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Turkish</span></a><button class="ZpqHX3kvsJIsR1QIc4kf" id="uk"
									data-testid="language-option-uk"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Українська</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Ukrainian</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="ur"
									data-testid="language-option-ur"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">اردو</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Urdu</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="vi"
									data-testid="language-option-vi"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">Tiếng Việt</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Vietnamese</span></button><button class="ZpqHX3kvsJIsR1QIc4kf" id="zh-CN"
									data-testid="language-option-zh-CN"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">简体中文</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Simplified Chinese</span></button><button class="ZpqHX3kvsJIsR1QIc4kf"
									id="zh-HK" data-testid="language-option-zh-HK"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">繁體中文 (香港)</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Chinese (Traditional) Hong Kong</span></button><button
									class="ZpqHX3kvsJIsR1QIc4kf" id="zh-TW" data-testid="language-option-zh-TW"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">中文</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Traditional Chinese</span></button><button class="ZpqHX3kvsJIsR1QIc4kf"
									id="zu" data-testid="language-option-zu"><span
										class="e-9911-text encore-text-body-medium encore-internal-color-text-base"
										data-encore-id="text">IsiZulu</span><span class="e-9911-text encore-text-body-medium"
										data-encore-id="text">Zulu</span></button></div>
						</div>
					</div>
				</div>
			</div>
			<div>
				<div class="XDe71TYCM1yakzJ0BVGp" role="presentation" data-open="closed">
					<section class="v2Lq3LdxHmr54XvZF1dS" role="dialog" aria-modal="true"
						aria-labelledby="country-selection-title">
						<div class="ObCtiQ5P3zY3bXBIkN2X"><button
								class="Button-sc-1dqy6lx-0 fprjoI e-9911-overflow-wrap-anywhere e-9911-button-tertiary--icon-only"
								aria-label="Close" data-encore-id="buttonTertiary"><span aria-hidden="true"
									class="e-9911-button__icon-wrapper"><svg data-encore-id="icon" role="img" aria-hidden="true"
										class="e-9911-icon e-9911-baseline" viewBox="0 0 16 16"
										style="--encore-icon-height: var(--encore-graphic-size-decorative-smaller); --encore-icon-width: var(--encore-graphic-size-decorative-smaller);">
										<path
											d="M2.47 2.47a.75.75 0 0 1 1.06 0L8 6.94l4.47-4.47a.75.75 0 1 1 1.06 1.06L9.06 8l4.47 4.47a.75.75 0 1 1-1.06 1.06L8 9.06l-4.47 4.47a.75.75 0 0 1-1.06-1.06L6.94 8 2.47 3.53a.75.75 0 0 1 0-1.06Z">
										</path>
									</svg></span></button></div>
						<div class="dsg9P8PEMDsVyt8ac3KD">
							<div class="BGK8c3q0Fvm7vdMU9Ov1">
								<h3 class="e-9911-text encore-text-body-medium-bold" data-encore-id="text" id="country-selection-title">
									Location</h3>
								<div class="e-9911-form-input-icon e-9911-baseline e-9911-form-input-icon--leading"
									data-encore-id="formInputIcon"
									style="--encore-form-input-icon-padding-leading: calc(24px + var(--encore-spacing-tighter, 12px) * 2);">
									<div class="e-9911-form-input-icon__icon e-9911-form-input-icon__icon--leading"><svg
											data-encore-id="icon" role="img" aria-hidden="true" class="e-9911-icon e-9911-baseline"
											viewBox="0 0 24 24">
											<path
												d="M10.533 1.27893C5.35215 1.27893 1.12598 5.41887 1.12598 10.5579C1.12598 15.697 5.35215 19.8369 10.533 19.8369C12.767 19.8369 14.8235 19.0671 16.4402 17.7794L20.7929 22.132C21.1834 22.5226 21.8166 22.5226 22.2071 22.132C22.5976 21.7415 22.5976 21.1083 22.2071 20.7178L17.8634 16.3741C19.1616 14.7849 19.94 12.7634 19.94 10.5579C19.94 5.41887 15.7138 1.27893 10.533 1.27893ZM3.12598 10.5579C3.12598 6.55226 6.42768 3.27893 10.533 3.27893C14.6383 3.27893 17.94 6.55226 17.94 10.5579C17.94 14.5636 14.6383 17.8369 10.533 17.8369C6.42768 17.8369 3.12598 14.5636 3.12598 10.5579Z">
											</path>
										</svg></div><input
										class="e-9911-form-input e-9911-baseline e-9911-form-control encore-text-body-medium"
										data-encore-id="formInput" placeholder="Search locations" value="">
								</div>
							</div>
							<ul class="yjfs8dP1IDOpoWAMk7_Q">
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/al">Albania</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/dz">Algeria</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ad">Andorra</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ao">Angola</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ag">Antigua and Barbuda</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ar">Argentina</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/am">Armenia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/au">Australia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/at">Austria</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/az">Azerbaijan</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bh">Bahrain</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bd">Bangladesh</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bb">Barbados</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/by">Belarus</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/be">Belgium</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bz">Belize</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bj">Benin</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bt">Bhutan</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bo">Bolivia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ba">Bosnia and Herzegovina</a>
								</li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bw">Botswana</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/br">Brazil</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bn">Brunei Darussalam</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bg">Bulgaria</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bf">Burkina Faso</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bi">Burundi</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/cv">Cabo Verde</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/kh">Cambodia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/cm">Cameroon</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ca">Canada</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/td">Chad</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/cl">Chile</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/co">Colombia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/km">Comoros</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/cr">Costa Rica</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ci">Cote d'Ivoire</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/hr">Croatia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/cw">Curacao</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/cy">Cyprus</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/cz">Czech Republic</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/cd">Democratic Republic of
										Congo</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/dk">Denmark</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/dj">Djibouti</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/dm">Dominica</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/do">Dominican Republic</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ec">Ecuador</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/eg">Egypt</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sv">El Salvador</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/gq">Equatorial Guinea</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ee">Estonia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sz">Eswatini</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/et">Ethiopia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/fj">Fiji</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/fi">Finland</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/fr">France</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ga">Gabon</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ge">Georgia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/de">Germany</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/gh">Ghana</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/gr">Greece</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/gd">Grenada</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/gt">Guatemala</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/gn">Guinea</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/gw">Guinea-Bissau</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/gy">Guyana</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ht">Haiti</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/hn">Honduras</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/hk">Hong Kong</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/hu">Hungary</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/is">Iceland</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/in">India</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/id">Indonesia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/iq">Iraq</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ie">Ireland</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/il">Israel</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/it">Italy</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/jm">Jamaica</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/jp">Japan</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/jo">Jordan</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/kz">Kazakhstan</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ke">Kenya</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ki">Kiribati</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/xk">Kosovo</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/kw">Kuwait</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/kg">Kyrgyz Republic</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/la">Lao PDR</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/lv">Latvia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/lb">Lebanon</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ls">Lesotho</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/lr">Liberia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ly">Libya</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/li">Liechtenstein</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/lt">Lithuania</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/lu">Luxembourg</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mo">Macao SAR, China</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mg">Madagascar</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mw">Malawi</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/my">Malaysia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mv">Maldives</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ml">Mali</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mt">Malta</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mh">Marshall Islands</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mr">Mauritania</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mu">Mauritius</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mx">Mexico</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/fm">Micronesia, Fed. Sts.</a>
								</li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/md">Moldova</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mc">Monaco</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mn">Mongolia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/me">Montenegro</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ma">Morocco</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mz">Mozambique</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/na">Namibia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/nr">Nauru</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/np">Nepal</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/nl">Netherlands</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/nz">New Zealand</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ni">Nicaragua</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ne">Niger</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ng">Nigeria</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/mk">North Macedonia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/no">Norway</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/om">Oman</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/pk">Pakistan</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/pw">Palau</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ps">Palestine</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/pa">Panama</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/pg">Papua New Guinea</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/py">Paraguay</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/pe">Peru</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ph">Philippines</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/pl">Poland</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/pt">Portugal</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/qa">Qatar</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/cg">Republic of the Congo</a>
								</li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ro">Romania</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/rw">Rwanda</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ws">Samoa</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sm">San Marino</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/st">Sao Tome and Principe</a>
								</li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sa">Saudi Arabia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sn">Senegal</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/rs">Serbia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sc">Seychelles</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sl">Sierra Leone</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sg">Singapore</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sk">Slovakia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/si">Slovenia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sb">Solomon Islands</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/za">South Africa</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/kr">South Korea</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/es">Spain</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/lk">Sri Lanka</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/kn">St. Kitts and Nevis</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/lc">St. Lucia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/vc">St. Vincent and the
										Grenadines</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/sr">Suriname</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/se">Sweden</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ch">Switzerland</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/tw">Taiwan</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/tj">Tajikistan</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/tz">Tanzania</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/th">Thailand</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/bs">The Bahamas</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/gm">The Gambia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/tl">Timor-Leste</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/tg">Togo</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/to">Tonga</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/tt">Trinidad and Tobago</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/tn">Tunisia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/tr">Turkey</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/tv">Tuvalu</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ug">Uganda</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ua">Ukraine</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ae">United Arab Emirates</a>
								</li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/gb">United Kingdom</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/us">United States</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/uy">Uruguay</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/uz">Uzbekistan</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/vu">Vanuatu</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/ve">Venezuela, RB</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/vn">Vietnam</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/zm">Zambia</a></li>
								<li><a draggable="false" class="yOchIz_U3btFceKrnMYt" href="/popular-in/zw">Zimbabwe</a></li>
							</ul>
						</div>
					</section>
				</div>
			</div>
		</div>
	</div><iframe style="display: none;" name="__tcfapiLocator" title="CMP Locator"></iframe>
	<div class="ReactModalPortal"></div>
	<div class="ReactModalPortal"></div>
	<div class="ReactModalPortal"></div>
	<div class="ReactModalPortal"></div>
	<div class="ReactModalPortal"></div>
	<div class="ReactModalPortal"></div>
	<div class="ReactModalPortal"></div>
	<div class="ReactModalPortal"></div><span id="live-region-3314" aria-live="polite" role="status"
		style="clip: rect(1px, 1px, 1px, 1px); height: 1px; overflow: hidden; position: absolute; white-space: nowrap; width: 1px">Now
		playing: Cool by Daniel Caesar</span>
</body>
<style class="stylus">
	@media (prefers-color-scheme: light) {
		:root {
			color-scheme: light;
			/* some borders on the playlist details */
		}

		:root ::selection {
			background-color: rgba(30, 102, 245, 0.3);
		}

		:root input::placeholder,
		:root textarea::placeholder {
			color: #6c6f85 !important;
		}

		:root .encore-dark-theme,
		:root .encore-dark-theme .encore-base-set,
		:root .encore-light-theme,
		:root .encore-light-theme .encore-base-set,
		:root .encore-dark-theme .encore-inverted-light-set {
			--background-base: #eff1f5;
			--background-highlight: #ccd0da;
			--background-press: #dce0e8;
			--background-elevated-base: #ccd0da;
			--background-elevated-highlight: #bcc0cc;
			--background-elevated-press: #dce0e8;
			--background-tinted-base: #dce0e8;
			--background-tinted-highlight: #e6e9ef;
			--background-tinted-press: #eff1f5;
			--background-unsafe-for-small-text-base: #eff1f5;
			--background-unsafe-for-small-text-highlight: #eff1f5;
			--background-unsafe-for-small-text-press: #eff1f5;
			--text-base: #4c4f69;
			--text-subdued: #5c5f77;
			--text-bright-accent: #1e66f5;
			--text-negative: #d20f39;
			--text-warning: #df8e1d;
			--text-positive: #1e66f5;
			--text-announcement: #209fb5;
			--essential-base: #4c4f69;
			--essential-subdued: #5c5f77;
			--essential-bright-accent: #1e66f5;
			--essential-negative: #d20f39;
			--essential-warning: #df8e1d;
			--essential-positive: #40a02b;
			--essential-announcement: #eff1f5;
			--decorative-base: #4c4f69;
			--decorative-subdued: #acb0be;
		}

		:root .encore-dark-theme .encore-inverted-light-set {
			--background-base: #bcc0cc;
			--background-highlight: #ccd0da;
			--background-press: #bcc0cc;
		}

		:root .encore-dark-theme .encore-bright-accent-set {
			--background-base: #1e66f5;
			--background-highlight: #1e66f5;
			--background-press: #1e66f5;
			--background-elevated-base: #1e66f5;
			--background-elevated-highlight: #1e66f5;
			--background-elevated-press: #1e66f5;
			--background-tinted-base: #1e66f5;
			--background-tinted-highlight: #1e66f5;
			--background-tinted-press: #1e66f5;
			--background-unsafe-for-small-text-base: #1e66f5;
			--background-unsafe-for-small-text-highlight: #1e66f5;
			--background-unsafe-for-small-text-press: #1e66f5;
			--decorative-subdued: #0a4ed6;
		}

		:root .encore-dark-theme .encore-over-media-set {
			--background-base: #e6e9ef;
			--background-highlight: #dce0e8;
			--background-press: #e6e9ef;
			--background-unsafe-for-small-text-base: #e6e9ef;
			--background-unsafe-for-small-text-highlight: #e6e9ef;
			--background-unsafe-for-small-text-press: #e6e9ef;
			--background-elevated-base: #dce0e8;
			--background-elevated-highlight: #dce0e8;
			--background-elevated-press: #e6e9ef;
			--background-tinted-base: #e6e9ef;
			--background-tinted-highlight: #e6e9ef;
			--background-tinted-press: #e6e9ef;
		}

		:root .T1xI1RTSFU7Wu94UuvE6 * {
			background: #ccd0da !important;
		}

		:root .bQthUEx0_U98DJkT1saO,
		:root .RVRoa p {
			color: #eff1f5 !important;
		}

		:root .encore-text {
			color: #4c4f69;
		}

		:root .ydlidzq2hSQrvGXn7yni {
			background: #4c4f69;
			color: #dce0e8;
		}

		:root .encore-dark-theme .encore-base-set>*,
		:root .encore-dark-theme>* {
			--parents-essential-base: #4c4f69;
		}

		:root .X8yW2lJbFCQfV5GjoRwL {
			--generic-tooltip-background-color: #e6e9ef;
		}

		:root .SboKmDrCTZng7t4EgNoM {
			background-color: #e6e9ef !important;
		}

		:root #main>*>*,
		:root .sqKERfoKl4KwrtHqcKOd,
		:root .HkbHLcqgUfXruL5xVi28,
		:root .uhDzVbFHyCQDH6WrWZaC,
		:root .pHrwZOFBdT8FNXnmcPPI {
			background: #dce0e8 !important;
		}

		:root .ePPpO_NuGDUxVRTw7y6W {
			border-color: #ccd0da;
		}

		:root .uWvwXlS0Da1bWsRX6KOw,
		:root .n5XwsUqagSoVk8oMiw1x {
			filter: saturate(0) brightness(1.3) !important;
		}

		:root .eoWRdH,
		:root .in4OjUTflcsoj9RUpf05 *,
		:root .gpNta6i8q3KYJC6WBZQC * {
			color: #6c6f85 !important;
		}

		:root ._EShSNaBK1wUIaZQFJJQ {
			box-shadow: 0 4px 20px #e6e9ef;
		}

		:root .gHImFiUWOg93pvTefeAD,
		:root .CoLO4pdSl8LGWyVZA00t {
			background: #eff1f5 !important;
		}

		:root .mjZrvVI3CxfHJXu7y0Lg,
		:root .coBkWVskipFo8KxLKief .T1xI1RTSFU7Wu94UuvE6 {
			background-color: #1e66f5 !important;
		}

		:root .ListRowTitle__LineClamp-sc-1xe2if1-0.lmgIvZ *,
		:root .EaTxqhHk6J4ecKHwpY5m *,
		:root .SboKmDrCTZng7t4EgNoM *,
		:root .MfVrtIzQJ7iZXfRWg6eM,
		:root .Ydwa1P5GkCggtLlSvphs,
		:root .Fb61sprjhh75aOITDnsJ *,
		:root .Ai_McRq9wJEYK21w8nX_ *,
		:root .QZhV0hWVKlExlKr266jo::placeholder,
		:root .JzZyf6OGCGtdscOZGt8Y.t6HIrX67Lp80Nj6tGauz *,
		:root .hfdkySA4kiUldFsPj9lD.ZcNcu7WZgOAz_Mkcoff3 *,
		:root .ListRowTitle__LineClamp-sc-1xe2if1-0 *,
		:root .FZhaXNtbN3Crwrgd0TA7.control-button,
		:root .COJ84QbXPrd4jkO1HU2N *,
		:root .zhQX2DOI2muMo8EKsZ6h,
		:root .MHIOvvlSYRmF7VAJDLWy,
		:root .JouuH90_RNAdTj0ZjcCA,
		:root .r9m6lHy7RyIPDzW1Youe,
		:root .PDPsYDh4ntfQE3B4duUI,
		:root .bfQ2S9bMXr_kJjqEfcwA *,
		:root .QO9loc33XC50mMRUCIvf,
		:root .G7zO58ORUHxcUw0sXktM,
		:root .rq2VQ5mb9SDAFWbBIUIn *,
		:root .lp9Tfm4rsM9_pfbIE0zd,
		:root .w6j_vX6SF5IxSXrrkYw5,
		:root .prGqQr33U0mG14TJ5V8a *,
		:root .BQD_pE0Nva_z6z7CvZww *,
		:root .W5cB_o0XkkU7Q8tlTGxq,
		:root .PGSe59fD1Hwc9yUM2d3U a,
		:root .jb9xD5ECTqKFK02qe3HZ *,
		:root .X8yW2lJbFCQfV5GjoRwL *,
		:root .tbvnCR3ZJxmAKY6nRPBe,
		:root .CmR9tHJ5ta6oWJlKBm3k *,
		:root .xgmjVLxjqfcXK5BV_XyN.fUYMR7LuRXv0KJWFvRZA,
		:root .DzWw3g4E_66wu9ktqn36 .home-active-icon,
		:root .Footer__StyledFooter-sc-xwm5vq-0 *,
		:root .DzWw3g4E_66wu9ktqn36 .search-active-icon,
		:root .dYnaPI,
		:root .home-active-icon,
		:root .zOsKPnD_9x3KJqQCSmAq,
		:root .beyOcd3p0PEzhrlKIbU1,
		:root .oORVTPvg6eTQflVKKgw8 {
			color: #4c4f69 !important;
		}

		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) .ObVor_8sQq5whKbtWs8a,
		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) .PAqIqZXvse_3h6sDVxU0,
		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) .UudGCx16EmBkuFPllvss a,
		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) .W676nknusnBt8sz19YVV,
		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) ._TH6YAXEzJtzSxhkGSqu,
		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) ._TH6YAXEzJtzSxhkGSqu a,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) .ObVor_8sQq5whKbtWs8a,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) .PAqIqZXvse_3h6sDVxU0,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) .UudGCx16EmBkuFPllvss a,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) .W676nknusnBt8sz19YVV,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) ._TH6YAXEzJtzSxhkGSqu,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) ._TH6YAXEzJtzSxhkGSqu a,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG .PAqIqZXvse_3h6sDVxU0,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG .UudGCx16EmBkuFPllvss,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG .UudGCx16EmBkuFPllvss a,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG ._TH6YAXEzJtzSxhkGSqu,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG ._TH6YAXEzJtzSxhkGSqu a,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG .ucB9avGYvzsmzXUOw0S7,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover .PAqIqZXvse_3h6sDVxU0,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover .UudGCx16EmBkuFPllvss,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover .UudGCx16EmBkuFPllvss a,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover ._TH6YAXEzJtzSxhkGSqu,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover ._TH6YAXEzJtzSxhkGSqu a,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover .ucB9avGYvzsmzXUOw0S7,
		:root .NPv26QCDgdnwsPOlYJmQ div:nth-child(2) {
			color: #5c5f77;
		}

		:root .VKCcyYujazVPj6VkksPM svg path {
			fill: #4c4f69;
		}

		:root .ThG4UqWk7ASXCMm69Opn,
		:root .BQD_pE0Nva_z6z7CvZww *,
		:root .k2ndSrHzhAsXBcLqRKYx * {
			color: #7c7f93 !important;
		}

		:root .gqYYMz8DkhaT3e44LcHQ span {
			color: #eff1f5;
		}

		:root *[class*="ButtonInner-sc-14ud5tc-0 GBxjH encore-bright-accent-set vq0lsCoYrDUDvkuUIaRg"] * {
			color: #dce0e8 !important;
			fill: #dce0e8 !important;
		}

		:root .bk509U3ZhZc9YBJAmoPB {
			background: #e6e9ef;
		}

		:root .HVCCFeUiHVwZVv74p34a *,
		:root .mXNT9H2GU7lDW4cGx0q1,
		:root .uV8q95GGAb2VDtL3gpYa {
			background: #ccd0da !important;
		}

		:root ._VADS4mdajCt5Yuf6KjW,
		:root .uJjmxe0T11dUVeW6Biz8 {
			background-color: #eff1f5;
		}

		:root .QO9loc33XC50mMRUCIvf {
			background-color: #ccd0da;
		}

		:root .QO9loc33XC50mMRUCIvf:focus {
			-webkit-box-shadow: 0 0 0 2px #4c4f69;
			box-shadow: 0 0 0 2px #4c4f69;
		}

		:root .QO9loc33XC50mMRUCIvf:hover {
			background-color: #bcc0cc;
		}

		:root .H6jh9Xd7DNOq3NsLDmCB:active,
		:root .H6jh9Xd7DNOq3NsLDmCB:focus,
		:root .H6jh9Xd7DNOq3NsLDmCB:hover {
			color: #4c4f69 !important;
		}

		:root .NbcaczStd8vD2rHWwaKv,
		:root .QZhV0hWVKlExlKr266jo {
			background-color: #ccd0da;
			color: #4c4f69;
		}

		:root div[role*="menuitem"] {
			background-color: #ccd0da !important;
		}

		:root .H6jh9Xd7DNOq3NsLDmCB,
		:root .htqz7Vb8mLJvGKTi1vrs,
		:root .dsbIME {
			color: #4c4f69;
		}

		:root .IconWrapper__Wrapper-sc-1hf1hjl-0 svg {
			color: #dce0e8 !important;
		}

		:root .kPpCsU {
			fill: #4c4f69;
		}

		:root .VgSbatGBB9XwTH2_dsxg .ql0zZd7giPXSnPg75NR0 {
			background: #eff1f5 !important;
			color: #4c4f69;
		}

		:root .HsbczDqu9qjcYr7EIdHR,
		:root .rovbQsmAS_mwvpKHaVhQ * {
			background: transparent !important;
		}

		:root .Z35BWOA10YGn5uc9YgAp,
		:root .pQmF4tvRpUeLWgPKUcW7 {
			background-color: #dce0e8;
		}

		:root .S4OmZ_IZexmZ5dasPqW5 {
			background-color: #1e66f5 !important;
		}

		:root .T1xI1RTSFU7Wu94UuvE6[style*="background-color:"] {
			background-color: #1e66f5 !important;
		}

		:root .fIvMht6B9HdROywMNJZ4.hIFR8WDm_54EEIa1gwpC {
			background-color: #1e66f5 !important;
		}

		:root .kpGMQq1KFz620g_BD_dS {
			background-color: #9ca0b0;
		}

		:root .link-subtle {
			color: #5c5f77;
		}

		:root .link-subtle:hover {
			color: #4c4f69;
		}

		:root .c0KyMkxeMCWQGE7cR8s_,
		:root .s58sp4t3h1uU9n_42KqD,
		:root .TextForLabel-sc-1jqya9m-0 span {
			color: #eff1f5 !important;
		}

		:root .LunqxlFIupJw_Dkx6mNx {
			background: #e6e9ef !important;
		}

		:root .bQthUEx0_U98DJkT1saO,
		:root .RVRoa p {
			color: #4c4f69;
		}

		:root .kmZeYl {
			background-color: #e6e9ef;
		}

		:root .kmZeYl:hover {
			background-color: #dce0e8;
		}

		:root #onetrust-banner-sdk {
			background-color: #eff1f5 !important;
			color: #4c4f69 !important;
		}

		:root #onetrust-policy-text,
		:root .ot-dpd-title,
		:root .onetrust-policy-title,
		:root .ot-text-bold {
			color: #4c4f69 !important;
		}

		:root .ot-dpd-desc,
		:root .ot-link-btn {
			color: #4c4f69 !important;
		}

		:root #onetrust-consent-sdk #onetrust-policy-title {
			color: #4c4f69 !important;
		}

		:root #onetrust-banner-sdk button {
			color: #4c4f69 !important;
		}

		:root #onetrust-pc-btn-handler {
			background-color: #eff1f5 !important;
		}

		:root #onetrust-consent-sdk #onetrust-pc-sdk,
		:root .ot-acc-txt,
		:root .ot-acc-grpdesc {
			background-color: #eff1f5 !important;
		}

		:root #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-title,
		:root #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-desc,
		:root #onetrust-consent-sdk #onetrust-pc-sdk h3,
		:root #onetrust-consent-sdk #onetrust-pc-sdk h5,
		:root #onetrust-consent-sdk #onetrust-pc-sdk h4,
		:root #onetrust-consent-sdk #onetrust-pc-sdk h6,
		:root #onetrust-consent-sdk #onetrust-pc-sdk h2,
		:root #onetrust-pc-sdk .ot-always-active,
		:root .ot-acc-txt,
		:root .ot-acc-grpdesc,
		:root #onetrust-consent-sdk #onetrust-pc-sdk p {
			color: #4c4f69 !important;
		}

		:root #onetrust-pc-sdk .ot-accordion-layout.ot-cat-item {
			border-color: #1e66f5 !important;
			border-radius: 8px;
		}

		:root #onetrust-consent-sdk #onetrust-pc-sdk button:not(#clear-filters-handler,
			.ot-close-icon,
			#filter-btn-handler,
			.ot-remove-objection-handler,
			.ot-obj-leg-btn-handler,
			[aria-expanded],
			.ot-link-btn) {
			background-color: #1e66f5 !important;
			border-color: #1e66f5 !important;
		}

		:root #onetrust-consent-sdk #onetrust-pc-sdk .ot-sel-all-hdr span {
			color: #4c4f69;
		}

		:root #onetrust-pc-sdk input[type="text"] {
			background-color: #e6e9ef !important;
			border-color: #1e66f5 !important;
		}

		:root #onetrust-pc-sdk .ot-pc-header,
		:root #onetrust-pc-sdk ul li {
			border-bottom-color: #1e66f5 !important;
			border-top-color: #1e66f5 !important;
		}

		:root #ot-ven-lst {
			border-top-color: #1e66f5 !important;
		}

		:root .ot-pc-footer {
			border-top-color: #1e66f5 !important;
		}

		:root #onetrust-pc-sdk li>button {
			border-top-color: #1e66f5 !important;
		}

		:root #onetrust-consent-sdk #onetrust-pc-sdk #ot-sel-blk {
			background-color: #eff1f5 !important;
		}

		:root .dz_h98rH9nZCwfPdnKgr {
			background-image: none;
		}

		:root .RfidWIoz8FON2WhFoItU {
			color: #4c4f69;
		}

		:root .cuLHaM {
			background-color: #eff1f5;
		}

		:root #Desktop_LeftSidebar_Id {
			background-color: transparent;
		}

		:root .y2UicQnlTq148rL8Y0jp {
			box-shadow: 0 6px 10px #e6e9ef;
		}

		:root .vnCew8qzJq3cVGlYFXRI {
			background-color: #4c4f69;
		}

		:root .vnCew8qzJq3cVGlYFXRI * {
			fill: #dce0e8;
		}

		:root .rovbQsmAS_mwvpKHaVhQ .PFgcCoJSWC3KjhZxHDYH * {
			fill: #4c4f69 !important;
		}

		:root .TywOcKZEqNynWecCiATc {
			--bg-color: #bcc0cc;
			--fg-color: #4c4f69;
			--is-active-fg-color: #1e66f5;
		}

		:root a {
			color: #1e66f5;
		}

		:root .Ng3dPPA2_1CFYkzPukjM {
			background: #1e66f5;
		}

		:root .KAZD28usA1vPz5GVpm63.EHxL6K_6WWDlTCZP6x5w::after {
			background-color: #1e66f5;
		}

		:root .tippy-box[data-theme~="activation"] {
			background-color: #1e66f5;
			color: #dce0e8;
		}

		:root .tippy-box[data-theme~="activation"] .c0KyMkxeMCWQGE7cR8s_ *,
		:root .tippy-box[data-theme~="activation"] .TextForLabel-sc-1jqya9m-0.kIsEKW {
			color: #dce0e8;
		}

		:root .YIJxiTuPgMQav316cRqP {
			--generic-tooltip-background-color: #ccd0da;
		}

		:root .tippy-arrow {
			color: #ccd0da !important;
		}

		:root .zrvvPyoxE6wQNqnu0yWA,
		:root .mjprSb2e1tKJpqwvgFSh,
		:root .jW4eWdr_LUeOXwPpKhWG {
			color: #4c4f69;
			background: #ccd0da;
		}

		:root input:checked~.Js64TOfWtHksI6TQ6knT {
			background: #1e66f5 !important;
		}

		:root .bXJ77rNIJ18Y0GfegQdr+label> :first-child {
			background: #4c4f69 !important;
		}

		:root .Z35BWOA10YGn5uc9YgAp:focus-within,
		:root .Z35BWOA10YGn5uc9YgAp:hover,
		:root .Z35BWOA10YGn5uc9YgAp[data-context-menu-open="true"] {
			background: #e6e9ef !important;
		}

		:root .wC9sIed7pfp47wZbmU6m:hover,
		:root .wC9sIed7pfp47wZbmU6m:not([aria-checked="true"]):focus {
			background: #ccd0da !important;
		}

		:root .DuEPSADpSwCcO880xjUG:not(:first-child)>.QgtQw2NJz7giDZxap2BB::before {
			border-color: #ccd0da;
		}

		:root .pSxFsY9Fgcj5f8Gf05mh,
		:root .qyKJPLjz8o4jnbk92JOn {
			background-color: rgba(220, 224, 232, 0.7);
		}

		:root .eG930DCaQXDFqjhxRGIs>* {
			background: #dce0e8 !important;
		}

		:root .IconWrapper__Wrapper-sc-1hf1hjl-0.fIXqki svg {
			color: #4c4f69 !important;
		}

		:root .IconWrapper__Wrapper-sc-1hf1hjl-0.bjlVXn svg.bneLcE {
			color: #eff1f5 !important;
		}

		:root .OF_3F0SQCsBtL1jSTlTA svg,
		:root .OF_3F0SQCsBtL1jSTlTA::after,
		:root .tP0mccyU1WAa7I9PevC1 svg,
		:root .tP0mccyU1WAa7I9PevC1::after {
			color: #1e66f5 !important;
		}

		:root .npv-up-next {
			background-color: #ccd0da !important;
		}

		:root .mbUrqWP55sK6zhspiR72 button {
			color: #4c4f69 !important;
		}

		:root .npv-lyrics__text-wrapper--previous p {
			color: #5c5f77 !important;
		}

		:root .npv-lyrics__text-wrapper--current p {
			color: #4c4f69 !important;
		}

		:root .npv-lyrics__text-wrapper--next p {
			color: #6c6f85 !important;
		}

		:root .npv-lyrics__text--credits {
			color: #4c4f69 !important;
		}

		:root div[data-tippy-root],
		:root #context-menu,
		:root #hover-or-focus-tooltip,
		:root .nYdM55iHFByRTzJUmx9X {
			border-radius: 8px;
			background-color: #ccd0da;
			color: #4c4f69;
		}
	}

	@media (prefers-color-scheme: dark) {
		:root {
			color-scheme: dark;
			/* some borders on the playlist details */
		}

		:root ::selection {
			background-color: rgba(137, 180, 250, 0.3);
		}

		:root input::placeholder,
		:root textarea::placeholder {
			color: #a6adc8 !important;
		}

		:root .encore-dark-theme,
		:root .encore-dark-theme .encore-base-set,
		:root .encore-light-theme,
		:root .encore-light-theme .encore-base-set,
		:root .encore-dark-theme .encore-inverted-light-set {
			--background-base: #1e1e2e;
			--background-highlight: #313244;
			--background-press: #11111b;
			--background-elevated-base: #313244;
			--background-elevated-highlight: #45475a;
			--background-elevated-press: #11111b;
			--background-tinted-base: #11111b;
			--background-tinted-highlight: #181825;
			--background-tinted-press: #1e1e2e;
			--background-unsafe-for-small-text-base: #1e1e2e;
			--background-unsafe-for-small-text-highlight: #1e1e2e;
			--background-unsafe-for-small-text-press: #1e1e2e;
			--text-base: #cdd6f4;
			--text-subdued: #bac2de;
			--text-bright-accent: #89b4fa;
			--text-negative: #f38ba8;
			--text-warning: #f9e2af;
			--text-positive: #89b4fa;
			--text-announcement: #74c7ec;
			--essential-base: #cdd6f4;
			--essential-subdued: #bac2de;
			--essential-bright-accent: #89b4fa;
			--essential-negative: #f38ba8;
			--essential-warning: #f9e2af;
			--essential-positive: #a6e3a1;
			--essential-announcement: #1e1e2e;
			--decorative-base: #cdd6f4;
			--decorative-subdued: #585b70;
		}

		:root .encore-dark-theme .encore-inverted-light-set {
			--background-base: #45475a;
			--background-highlight: #313244;
			--background-press: #45475a;
		}

		:root .encore-dark-theme .encore-bright-accent-set {
			--background-base: #89b4fa;
			--background-highlight: #89b4fa;
			--background-press: #89b4fa;
			--background-elevated-base: #89b4fa;
			--background-elevated-highlight: #89b4fa;
			--background-elevated-press: #89b4fa;
			--background-tinted-base: #89b4fa;
			--background-tinted-highlight: #89b4fa;
			--background-tinted-press: #89b4fa;
			--background-unsafe-for-small-text-base: #89b4fa;
			--background-unsafe-for-small-text-highlight: #89b4fa;
			--background-unsafe-for-small-text-press: #89b4fa;
			--decorative-subdued: #5895f8;
		}

		:root .encore-dark-theme .encore-over-media-set {
			--background-base: #181825;
			--background-highlight: #11111b;
			--background-press: #181825;
			--background-unsafe-for-small-text-base: #181825;
			--background-unsafe-for-small-text-highlight: #181825;
			--background-unsafe-for-small-text-press: #181825;
			--background-elevated-base: #11111b;
			--background-elevated-highlight: #11111b;
			--background-elevated-press: #181825;
			--background-tinted-base: #181825;
			--background-tinted-highlight: #181825;
			--background-tinted-press: #181825;
		}

		:root .encore-text {
			color: #cdd6f4;
		}

		:root .ydlidzq2hSQrvGXn7yni {
			background: #cdd6f4;
			color: #11111b;
		}

		:root .encore-dark-theme .encore-base-set>*,
		:root .encore-dark-theme>* {
			--parents-essential-base: #cdd6f4;
		}

		:root .X8yW2lJbFCQfV5GjoRwL {
			--generic-tooltip-background-color: #181825;
		}

		:root .SboKmDrCTZng7t4EgNoM {
			background-color: #181825 !important;
		}

		:root #main>*>*,
		:root .sqKERfoKl4KwrtHqcKOd,
		:root .HkbHLcqgUfXruL5xVi28,
		:root .uhDzVbFHyCQDH6WrWZaC,
		:root .pHrwZOFBdT8FNXnmcPPI {
			background: #11111b !important;
		}

		:root .ePPpO_NuGDUxVRTw7y6W {
			border-color: #313244;
		}

		:root .uWvwXlS0Da1bWsRX6KOw,
		:root .n5XwsUqagSoVk8oMiw1x {
			filter: saturate(0) brightness(1.3) !important;
		}

		:root .eoWRdH,
		:root .in4OjUTflcsoj9RUpf05 *,
		:root .gpNta6i8q3KYJC6WBZQC * {
			color: #a6adc8 !important;
		}

		:root ._EShSNaBK1wUIaZQFJJQ {
			box-shadow: 0 4px 20px #181825;
		}

		:root .gHImFiUWOg93pvTefeAD,
		:root .CoLO4pdSl8LGWyVZA00t {
			background: #1e1e2e !important;
		}

		:root .mjZrvVI3CxfHJXu7y0Lg,
		:root .coBkWVskipFo8KxLKief .T1xI1RTSFU7Wu94UuvE6 {
			background-color: #89b4fa !important;
		}

		:root .ListRowTitle__LineClamp-sc-1xe2if1-0.lmgIvZ *,
		:root .EaTxqhHk6J4ecKHwpY5m *,
		:root .SboKmDrCTZng7t4EgNoM *,
		:root .MfVrtIzQJ7iZXfRWg6eM,
		:root .Ydwa1P5GkCggtLlSvphs,
		:root .Fb61sprjhh75aOITDnsJ *,
		:root .Ai_McRq9wJEYK21w8nX_ *,
		:root .QZhV0hWVKlExlKr266jo::placeholder,
		:root .JzZyf6OGCGtdscOZGt8Y.t6HIrX67Lp80Nj6tGauz *,
		:root .hfdkySA4kiUldFsPj9lD.ZcNcu7WZgOAz_Mkcoff3 *,
		:root .ListRowTitle__LineClamp-sc-1xe2if1-0 *,
		:root .FZhaXNtbN3Crwrgd0TA7.control-button,
		:root .COJ84QbXPrd4jkO1HU2N *,
		:root .zhQX2DOI2muMo8EKsZ6h,
		:root .MHIOvvlSYRmF7VAJDLWy,
		:root .JouuH90_RNAdTj0ZjcCA,
		:root .r9m6lHy7RyIPDzW1Youe,
		:root .PDPsYDh4ntfQE3B4duUI,
		:root .bfQ2S9bMXr_kJjqEfcwA *,
		:root .QO9loc33XC50mMRUCIvf,
		:root .G7zO58ORUHxcUw0sXktM,
		:root .rq2VQ5mb9SDAFWbBIUIn *,
		:root .lp9Tfm4rsM9_pfbIE0zd,
		:root .w6j_vX6SF5IxSXrrkYw5,
		:root .prGqQr33U0mG14TJ5V8a *,
		:root .BQD_pE0Nva_z6z7CvZww *,
		:root .W5cB_o0XkkU7Q8tlTGxq,
		:root .PGSe59fD1Hwc9yUM2d3U a,
		:root .jb9xD5ECTqKFK02qe3HZ *,
		:root .X8yW2lJbFCQfV5GjoRwL *,
		:root .tbvnCR3ZJxmAKY6nRPBe,
		:root .CmR9tHJ5ta6oWJlKBm3k *,
		:root .xgmjVLxjqfcXK5BV_XyN.fUYMR7LuRXv0KJWFvRZA,
		:root .DzWw3g4E_66wu9ktqn36 .home-active-icon,
		:root .Footer__StyledFooter-sc-xwm5vq-0 *,
		:root .DzWw3g4E_66wu9ktqn36 .search-active-icon,
		:root .dYnaPI,
		:root .home-active-icon,
		:root .zOsKPnD_9x3KJqQCSmAq,
		:root .beyOcd3p0PEzhrlKIbU1,
		:root .oORVTPvg6eTQflVKKgw8 {
			color: #cdd6f4 !important;
		}

		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) .ObVor_8sQq5whKbtWs8a,
		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) .PAqIqZXvse_3h6sDVxU0,
		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) .UudGCx16EmBkuFPllvss a,
		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) .W676nknusnBt8sz19YVV,
		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) ._TH6YAXEzJtzSxhkGSqu,
		:root .IjYxRc5luMiDPhKhZVUH:focus-within:not(.tH1iuxCV8NexP4pzEBa4) ._TH6YAXEzJtzSxhkGSqu a,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) .ObVor_8sQq5whKbtWs8a,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) .PAqIqZXvse_3h6sDVxU0,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) .UudGCx16EmBkuFPllvss a,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) .W676nknusnBt8sz19YVV,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) ._TH6YAXEzJtzSxhkGSqu,
		:root .IjYxRc5luMiDPhKhZVUH:hover:not(.tH1iuxCV8NexP4pzEBa4) ._TH6YAXEzJtzSxhkGSqu a,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG .PAqIqZXvse_3h6sDVxU0,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG .UudGCx16EmBkuFPllvss,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG .UudGCx16EmBkuFPllvss a,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG ._TH6YAXEzJtzSxhkGSqu,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG ._TH6YAXEzJtzSxhkGSqu a,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG .ucB9avGYvzsmzXUOw0S7,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover .PAqIqZXvse_3h6sDVxU0,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover .UudGCx16EmBkuFPllvss,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover .UudGCx16EmBkuFPllvss a,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover ._TH6YAXEzJtzSxhkGSqu,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover ._TH6YAXEzJtzSxhkGSqu a,
		:root .IjYxRc5luMiDPhKhZVUH.JgERXNoqNav5zOHiZGfG:hover .ucB9avGYvzsmzXUOw0S7,
		:root .NPv26QCDgdnwsPOlYJmQ div:nth-child(2) {
			color: #bac2de;
		}

		:root .VKCcyYujazVPj6VkksPM svg path {
			fill: #cdd6f4;
		}

		:root .ThG4UqWk7ASXCMm69Opn,
		:root .BQD_pE0Nva_z6z7CvZww *,
		:root .k2ndSrHzhAsXBcLqRKYx * {
			color: #9399b2 !important;
		}

		:root .gqYYMz8DkhaT3e44LcHQ span {
			color: #1e1e2e;
		}

		:root *[class*="ButtonInner-sc-14ud5tc-0 GBxjH encore-bright-accent-set vq0lsCoYrDUDvkuUIaRg"] * {
			color: #11111b !important;
			fill: #11111b !important;
		}

		:root .bk509U3ZhZc9YBJAmoPB {
			background: #181825;
		}

		:root .HVCCFeUiHVwZVv74p34a *,
		:root .mXNT9H2GU7lDW4cGx0q1,
		:root .uV8q95GGAb2VDtL3gpYa {
			background: #313244 !important;
		}

		:root ._VADS4mdajCt5Yuf6KjW,
		:root .uJjmxe0T11dUVeW6Biz8 {
			background-color: #1e1e2e;
		}

		:root .QO9loc33XC50mMRUCIvf {
			background-color: #313244;
		}

		:root .QO9loc33XC50mMRUCIvf:focus {
			-webkit-box-shadow: 0 0 0 2px #cdd6f4;
			box-shadow: 0 0 0 2px #cdd6f4;
		}

		:root .QO9loc33XC50mMRUCIvf:hover {
			background-color: #45475a;
		}

		:root .H6jh9Xd7DNOq3NsLDmCB:active,
		:root .H6jh9Xd7DNOq3NsLDmCB:focus,
		:root .H6jh9Xd7DNOq3NsLDmCB:hover {
			color: #cdd6f4 !important;
		}

		:root .NbcaczStd8vD2rHWwaKv,
		:root .QZhV0hWVKlExlKr266jo {
			background-color: #313244;
			color: #cdd6f4;
		}

		:root div[role*="menuitem"] {
			background-color: #313244 !important;
		}

		:root .H6jh9Xd7DNOq3NsLDmCB,
		:root .htqz7Vb8mLJvGKTi1vrs,
		:root .dsbIME {
			color: #cdd6f4;
		}

		:root .IconWrapper__Wrapper-sc-1hf1hjl-0 svg {
			color: #11111b !important;
		}

		:root .kPpCsU {
			fill: #cdd6f4;
		}

		:root .VgSbatGBB9XwTH2_dsxg .ql0zZd7giPXSnPg75NR0 {
			background: #1e1e2e !important;
			color: #cdd6f4;
		}

		:root .HsbczDqu9qjcYr7EIdHR,
		:root .rovbQsmAS_mwvpKHaVhQ * {
			background: transparent !important;
		}

		:root .Z35BWOA10YGn5uc9YgAp,
		:root .pQmF4tvRpUeLWgPKUcW7 {
			background-color: #11111b;
		}

		:root .S4OmZ_IZexmZ5dasPqW5 {
			background-color: #89b4fa !important;
		}

		:root .T1xI1RTSFU7Wu94UuvE6[style*="background-color:"] {
			background-color: #89b4fa !important;
		}

		:root .fIvMht6B9HdROywMNJZ4.hIFR8WDm_54EEIa1gwpC {
			background-color: #89b4fa !important;
		}

		:root .kpGMQq1KFz620g_BD_dS {
			background-color: #6c7086;
		}

		:root .link-subtle {
			color: #bac2de;
		}

		:root .link-subtle:hover {
			color: #cdd6f4;
		}

		:root .c0KyMkxeMCWQGE7cR8s_,
		:root .s58sp4t3h1uU9n_42KqD,
		:root .TextForLabel-sc-1jqya9m-0 span {
			color: #1e1e2e !important;
		}

		:root .LunqxlFIupJw_Dkx6mNx {
			background: #181825 !important;
		}

		:root .bQthUEx0_U98DJkT1saO,
		:root .RVRoa p {
			color: #cdd6f4;
		}

		:root .kmZeYl {
			background-color: #181825;
		}

		:root .kmZeYl:hover {
			background-color: #11111b;
		}

		:root #onetrust-banner-sdk {
			background-color: #1e1e2e !important;
			color: #cdd6f4 !important;
		}

		:root #onetrust-policy-text,
		:root .ot-dpd-title,
		:root .onetrust-policy-title,
		:root .ot-text-bold {
			color: #cdd6f4 !important;
		}

		:root .ot-dpd-desc,
		:root .ot-link-btn {
			color: #cdd6f4 !important;
		}

		:root #onetrust-consent-sdk #onetrust-policy-title {
			color: #cdd6f4 !important;
		}

		:root #onetrust-banner-sdk button {
			color: #cdd6f4 !important;
		}

		:root #onetrust-pc-btn-handler {
			background-color: #1e1e2e !important;
		}

		:root #onetrust-consent-sdk #onetrust-pc-sdk,
		:root .ot-acc-txt,
		:root .ot-acc-grpdesc {
			background-color: #1e1e2e !important;
		}

		:root #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-title,
		:root #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-desc,
		:root #onetrust-consent-sdk #onetrust-pc-sdk h3,
		:root #onetrust-consent-sdk #onetrust-pc-sdk h5,
		:root #onetrust-consent-sdk #onetrust-pc-sdk h4,
		:root #onetrust-consent-sdk #onetrust-pc-sdk h6,
		:root #onetrust-consent-sdk #onetrust-pc-sdk h2,
		:root #onetrust-pc-sdk .ot-always-active,
		:root .ot-acc-txt,
		:root .ot-acc-grpdesc,
		:root #onetrust-consent-sdk #onetrust-pc-sdk p {
			color: #cdd6f4 !important;
		}

		:root #onetrust-pc-sdk .ot-accordion-layout.ot-cat-item {
			border-color: #89b4fa !important;
			border-radius: 8px;
		}

		:root #onetrust-consent-sdk #onetrust-pc-sdk button:not(#clear-filters-handler,
			.ot-close-icon,
			#filter-btn-handler,
			.ot-remove-objection-handler,
			.ot-obj-leg-btn-handler,
			[aria-expanded],
			.ot-link-btn) {
			background-color: #89b4fa !important;
			border-color: #89b4fa !important;
		}

		:root #onetrust-consent-sdk #onetrust-pc-sdk .ot-sel-all-hdr span {
			color: #cdd6f4;
		}

		:root #onetrust-pc-sdk input[type="text"] {
			background-color: #181825 !important;
			border-color: #89b4fa !important;
		}

		:root #onetrust-pc-sdk .ot-pc-header,
		:root #onetrust-pc-sdk ul li {
			border-bottom-color: #89b4fa !important;
			border-top-color: #89b4fa !important;
		}

		:root #ot-ven-lst {
			border-top-color: #89b4fa !important;
		}

		:root .ot-pc-footer {
			border-top-color: #89b4fa !important;
		}

		:root #onetrust-pc-sdk li>button {
			border-top-color: #89b4fa !important;
		}

		:root #onetrust-consent-sdk #onetrust-pc-sdk #ot-sel-blk {
			background-color: #1e1e2e !important;
		}

		:root .dz_h98rH9nZCwfPdnKgr {
			background-image: none;
		}

		:root .RfidWIoz8FON2WhFoItU {
			color: #cdd6f4;
		}

		:root .cuLHaM {
			background-color: #1e1e2e;
		}

		:root #Desktop_LeftSidebar_Id {
			background-color: transparent;
		}

		:root .y2UicQnlTq148rL8Y0jp {
			box-shadow: 0 6px 10px #181825;
		}

		:root .vnCew8qzJq3cVGlYFXRI {
			background-color: #cdd6f4;
		}

		:root .vnCew8qzJq3cVGlYFXRI * {
			fill: #11111b;
		}

		:root .rovbQsmAS_mwvpKHaVhQ .PFgcCoJSWC3KjhZxHDYH * {
			fill: #cdd6f4 !important;
		}

		:root .TywOcKZEqNynWecCiATc {
			--bg-color: #45475a;
			--fg-color: #cdd6f4;
			--is-active-fg-color: #89b4fa;
		}

		:root a {
			color: #89b4fa;
		}

		:root .Ng3dPPA2_1CFYkzPukjM {
			background: #89b4fa;
		}

		:root .KAZD28usA1vPz5GVpm63.EHxL6K_6WWDlTCZP6x5w::after {
			background-color: #89b4fa;
		}

		:root .tippy-box[data-theme~="activation"] {
			background-color: #89b4fa;
			color: #11111b;
		}

		:root .tippy-box[data-theme~="activation"] .c0KyMkxeMCWQGE7cR8s_ *,
		:root .tippy-box[data-theme~="activation"] .TextForLabel-sc-1jqya9m-0.kIsEKW {
			color: #11111b;
		}

		:root .YIJxiTuPgMQav316cRqP {
			--generic-tooltip-background-color: #313244;
		}

		:root .tippy-arrow {
			color: #313244 !important;
		}

		:root .zrvvPyoxE6wQNqnu0yWA,
		:root .mjprSb2e1tKJpqwvgFSh,
		:root .jW4eWdr_LUeOXwPpKhWG {
			color: #cdd6f4;
			background: #313244;
		}

		:root input:checked~.Js64TOfWtHksI6TQ6knT {
			background: #89b4fa !important;
		}

		:root .bXJ77rNIJ18Y0GfegQdr+label> :first-child {
			background: #cdd6f4 !important;
		}

		:root .Z35BWOA10YGn5uc9YgAp:focus-within,
		:root .Z35BWOA10YGn5uc9YgAp:hover,
		:root .Z35BWOA10YGn5uc9YgAp[data-context-menu-open="true"] {
			background: #181825 !important;
		}

		:root .wC9sIed7pfp47wZbmU6m:hover,
		:root .wC9sIed7pfp47wZbmU6m:not([aria-checked="true"]):focus {
			background: #313244 !important;
		}

		:root .DuEPSADpSwCcO880xjUG:not(:first-child)>.QgtQw2NJz7giDZxap2BB::before {
			border-color: #313244;
		}

		:root .pSxFsY9Fgcj5f8Gf05mh,
		:root .qyKJPLjz8o4jnbk92JOn {
			background-color: rgba(17, 17, 27, 0.7);
		}

		:root .eG930DCaQXDFqjhxRGIs>* {
			background: #11111b !important;
		}

		:root .IconWrapper__Wrapper-sc-1hf1hjl-0.fIXqki svg {
			color: #cdd6f4 !important;
		}

		:root .IconWrapper__Wrapper-sc-1hf1hjl-0.bjlVXn svg.bneLcE {
			color: #1e1e2e !important;
		}

		:root .OF_3F0SQCsBtL1jSTlTA svg,
		:root .OF_3F0SQCsBtL1jSTlTA::after,
		:root .tP0mccyU1WAa7I9PevC1 svg,
		:root .tP0mccyU1WAa7I9PevC1::after {
			color: #89b4fa !important;
		}

		:root .npv-up-next {
			background-color: #313244 !important;
		}

		:root .mbUrqWP55sK6zhspiR72 button {
			color: #cdd6f4 !important;
		}

		:root .npv-lyrics__text-wrapper--previous p {
			color: #bac2de !important;
		}

		:root .npv-lyrics__text-wrapper--current p {
			color: #cdd6f4 !important;
		}

		:root .npv-lyrics__text-wrapper--next p {
			color: #a6adc8 !important;
		}

		:root .npv-lyrics__text--credits {
			color: #cdd6f4 !important;
		}

		:root div[data-tippy-root],
		:root #context-menu,
		:root #hover-or-focus-tooltip,
		:root .nYdM55iHFByRTzJUmx9X {
			border-radius: 8px;
			background-color: #313244;
			color: #cdd6f4;
		}
	}
</style>

</html>''')