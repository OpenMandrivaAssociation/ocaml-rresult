%undefine _debugsource_packages

Name:           ocaml-rresult
Version:        0.7.0
Release:        1
Summary:        Result value combinators for OCaml

License:        ISC
URL:            https://erratique.ch/software/rresult
VCS:            git:https://erratique.ch/repos/rresult.git
Source:         %{url}/releases/rresult-%{version}.tbz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-topkg-devel >= 1.0.3

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Warnings

%description
Rresult is an OCaml module for handling computation results and errors
in an explicit and declarative manner without resorting to exceptions.
It defines combinators to operate on the values of the result type
available from OCaml 4.03 in the standard library.

OCaml 4.08 provides the Stdlib.Result module which you should prefer to
Rresult.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n rresult-%{version}

%build
ocaml pkg/pkg.ml build --dev-pkg false --tests true

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel
%if %{with docs}
%doc _build/default/_doc/*
%endif
