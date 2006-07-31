Summary:	French resources for SeaMonkey
Summary(pl):	Francuskie pliki j�zykowe dla SeaMonkeya
Name:		seamonkey-lang-fr
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.fr-FR.langpack.xpi
# Source0-md5:	7ec7b9f5662757540b34798ad256f7f7
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-fr-FR-0.9x.xpi
# Source1-md5:	e8d57b69a0bb74d0f28e940b067280db
Source2:	gen-installed-chrome.sh
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
Francuskie pliki j�zykowe dla SeaMonkeya.

%prep
%setup -q -c
unzip -o %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale bin/chrome/{FR,fr-FR,fr-unix}.jar \
	> lang-fr-installed-chrome.txt
./gen-installed-chrome.sh locale chrome/enigmail-fr-FR.jar \
	>> lang-fr-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{FR,fr-FR,fr-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install chrome/enigmail-fr-FR.jar $RPM_BUILD_ROOT%{_chromedir}
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
%{_chromedir}/enigmail-fr-FR.jar
%{_chromedir}/lang-fr-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/googlefr.*
%{_datadir}/seamonkey/defaults/isp/FR
%{_datadir}/seamonkey/defaults/messenger/FR
%{_datadir}/seamonkey/defaults/profile/FR
%{_datadir}/seamonkey/myspell/*
