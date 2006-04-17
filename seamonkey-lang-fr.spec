Summary:	French resources for SeaMonkey
Summary(pl):	Francuskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-fr
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.fr-FR.langpack.xpi
# Source0-md5:	ee0c47c755fad435fd886455000acfa2
Source1:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
French resources for SeaMonkey.

%description -l pl
Francuskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c
install %{SOURCE1} .
./gen-installed-chrome.sh locale bin/chrome/{FR,fr-FR,fr-unix}.jar \
	> lang-fr-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{FR,fr-FR,fr-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-fr-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r bin/{defaults,searchplugins} $RPM_BUILD_ROOT%{_datadir}/seamonkey
cp -r bin/components/myspell $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/fr-FR.jar
%{_chromedir}/fr-unix.jar
%{_chromedir}/FR.jar
%{_chromedir}/lang-fr-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/googlefr.*
%{_datadir}/seamonkey/defaults/isp/FR
%{_datadir}/seamonkey/defaults/messenger/FR
%{_datadir}/seamonkey/defaults/profile/FR
%{_datadir}/seamonkey/myspell/*
