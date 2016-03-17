Summary:	Historically compatible Doom engine
Name:		chocolate-doom
Version:	2.2.0
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://www.chocolate-doom.org/downloads/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8b32745d113f25fd0985a03a5d632ba5
Source1:	%{name}.appdata.xml
URL:		http://chocolate-doom.org/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libsamplerate-devel
BuildRequires:	python
BuildRequires:	python-modules
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Provides:	bundled(md5-plumb)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chocolate Doom is a game engine that aims to accurately reproduce the
experience of playing vanilla Doom. It is a conservative, historically
accurate Doom source port, which is compatible with the thousands of
mods and levels that were made before the Doom source code was
released. Rather than flashy new graphics, Chocolate Doom's main
features are its accurate reproduction of the game as it was played in
the 1990s.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	iconsdir=%{_iconsdir}/hicolor/64x64/apps \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf docs
install -d docs
mv $RPM_BUILD_ROOT%{_docdir}/chocolate-{doom,heretic,hexen,strife} docs

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/appdata}
mv $RPM_BUILD_ROOT%{_prefix}/games/* $RPM_BUILD_ROOT%{_bindir}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/chocolate-heretic.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/chocolate-hexen.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/chocolate-strife.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/screensavers/chocolate-doom-screensaver.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS NOT-BUGS README
%doc docs/*
%attr(755,root,root) %{_bindir}/chocolate-doom
%attr(755,root,root) %{_bindir}/chocolate-server
%attr(755,root,root) %{_bindir}/chocolate-doom-setup
%attr(755,root,root) %{_bindir}/chocolate-heretic
%attr(755,root,root) %{_bindir}/chocolate-heretic-setup
%attr(755,root,root) %{_bindir}/chocolate-hexen
%attr(755,root,root) %{_bindir}/chocolate-hexen-setup
%attr(755,root,root) %{_bindir}/chocolate-strife
%attr(755,root,root) %{_bindir}/chocolate-strife-setup
%{_datadir}/appdata/*.appdata.xml
%{_desktopdir}/chocolate-doom.desktop
%{_desktopdir}/chocolate-setup.desktop
%{_desktopdir}/screensavers/chocolate-doom-screensaver.desktop
%{_desktopdir}/chocolate-heretic.desktop
%{_desktopdir}/chocolate-hexen.desktop
%{_desktopdir}/chocolate-strife.desktop
%{_iconsdir}/hicolor/*/apps/chocolate-doom.png
%{_iconsdir}/hicolor/*/apps/chocolate-setup.png
%{_mandir}/man5/chocolate-doom.cfg.5*
%{_mandir}/man5/chocolate-heretic.cfg.5*
%{_mandir}/man5/chocolate-hexen.cfg.5*
%{_mandir}/man5/chocolate-strife.cfg.5*
%{_mandir}/man5/default.cfg.5*
%{_mandir}/man5/heretic.cfg.5*
%{_mandir}/man5/hexen.cfg.5*
%{_mandir}/man5/strife.cfg.5*
%{_mandir}/man6/chocolate-doom.6*
%{_mandir}/man6/chocolate-server.6*
%{_mandir}/man6/chocolate-setup.6*
%{_mandir}/man6/chocolate-doom-setup.6*
%{_mandir}/man6/chocolate-heretic-setup.6*
%{_mandir}/man6/chocolate-heretic.6*
%{_mandir}/man6/chocolate-hexen-setup.6*
%{_mandir}/man6/chocolate-hexen.6*
%{_mandir}/man6/chocolate-strife-setup.6*
%{_mandir}/man6/chocolate-strife.6*
