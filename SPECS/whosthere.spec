%define debug_package %{nil}

%global gh_user ramonvermeulen
%global build_date %(date +%%Y%%m%%d)

Name:           whosthere
Version:        0.4.0
Release:        1%{?dist}
Summary:        Knock Knock.. who's there?
Group:          Applications/System
License:        GNU
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang

%description
Local Area Network discovery tool with a modern Terminal User Interface
(TUI) written in Go. Discover, explore, and understand your LAN in an
intuitive way. Knock Knock.. who's there?

%prep
%setup -q -n %{name}-%{version}

%build
%define ldflags -s -w -X main.versionStr=v%{version} -X main.commitStr=%{version} -X main.dateStr=%{build_date}
CGO_ENABLED=0 go build -ldflags '%{ldflags}' -o ./bin/%{name} .

%install
install -Dm0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Wed Jan 28 2026 Jamie Curnow <jc@jc21.com> - 0.4.0-1
- https://github.com/ramonvermeulen/whosthere/releases/tag/v0.4.0
